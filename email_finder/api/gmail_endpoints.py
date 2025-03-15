"""
Gmail API Endpoints for Email Finder System.

This module provides API endpoints for Gmail authentication and email sending.
"""

import os
import json
import logging
from typing import Dict, Any, Optional
from flask import Blueprint, request, redirect, jsonify, url_for, current_app
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.errors import HttpError

from email_finder.integrations.gmail_auth import (
    get_oauth2_flow,
    store_tokens,
    get_tokens,
    verify_gmail_connection,
    disconnect_gmail,
    send_email
)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create Blueprint
gmail_bp = Blueprint('gmail', __name__, url_prefix='/api/email-gmail')

@gmail_bp.route('', methods=['GET'])
def gmail_auth():
    """
    Initiates the Gmail OAuth flow.
    
    Redirects to Google's consent screen with the required scopes.
    
    Query Parameters:
        client_id: The client ID to associate with this authentication
    
    Returns:
        Redirect to Google's consent screen
    """
    try:
        # Get client ID from query parameters
        client_id = request.args.get('client_id')
        
        if not client_id:
            logger.error("No client_id provided for Gmail auth")
            return redirect(url_for('gmail.auth_callback', error='Client ID is required'))
        
        # Build redirect URI
        redirect_uri = url_for('gmail.auth_callback', _external=True)
        
        # Initialize OAuth flow
        flow = get_oauth2_flow(redirect_uri)
        
        # Generate authorization URL with required scopes
        auth_url = flow.authorization_url(
            access_type='offline',
            prompt='consent',
            state=client_id
        )[0]
        
        logger.info(f"Generated Gmail auth URL for client: {client_id}")
        return redirect(auth_url)
    except Exception as e:
        logger.error(f"Error generating Gmail auth URL: {str(e)}")
        return redirect(url_for('gmail.auth_callback', error=f'Failed to generate authorization URL: {str(e)}'))

@gmail_bp.route('/oauth-callback', methods=['GET'])
def auth_callback():
    """
    Handles the callback from Google with the authorization code.
    
    Exchanges the authorization code for tokens and stores them in Firestore.
    
    Query Parameters:
        code: The authorization code from Google
        state: The client ID passed in the state parameter
        error: Error message from Google (if any)
    
    Returns:
        Redirect to success or error page
    """
    try:
        # Parse query parameters
        code = request.args.get('code')
        state = request.args.get('state')  # Contains the client ID
        error = request.args.get('error')
        
        # Check for OAuth errors
        if error:
            logger.error(f"Google returned an error: {error}")
            return redirect('/gmail-auth-result.html?error=Authorization+was+denied')
        
        # Validate required parameters
        if not code:
            logger.error("Missing authorization code")
            return redirect('/gmail-auth-result.html?error=Missing+authorization+code')
        
        if not state:
            logger.error("Missing state parameter")
            return redirect('/gmail-auth-result.html?error=Missing+state+parameter')
        
        # Build redirect URI (must match the one used in the auth request)
        redirect_uri = url_for('gmail.auth_callback', _external=True)
        
        # Initialize OAuth flow
        flow = get_oauth2_flow(redirect_uri)
        
        # Exchange code for tokens
        logger.info(f"Exchanging authorization code for tokens for client: {state}")
        flow.fetch_token(code=code)
        tokens = flow.credentials.to_json()
        tokens_dict = json.loads(tokens)
        
        # Store tokens in Firestore
        success = store_tokens(state, tokens_dict)
        
        if not success:
            logger.error(f"Failed to store Gmail tokens for client: {state}")
            return redirect('/gmail-auth-result.html?error=Failed+to+store+tokens')
        
        # Redirect to success page
        logger.info(f"Gmail authentication successful for client: {state}")
        return redirect(f'/gmail-auth-result.html?message=Gmail+connected+successfully&client_id={state}')
    except Exception as e:
        logger.error(f"Error in Gmail auth callback: {str(e)}")
        return redirect(f'/gmail-auth-result.html?error={str(e)}')

@gmail_bp.route('/status', methods=['GET'])
def connection_status():
    """
    Checks the status of a client's Gmail connection.
    
    Query Parameters:
        client_id: The client ID to check
    
    Returns:
        JSON with connection status
    """
    try:
        client_id = request.args.get('client_id')
        
        if not client_id:
            return jsonify({
                'connected': False,
                'error': 'Client ID is required'
            }), 400
        
        status = verify_gmail_connection(client_id)
        return jsonify(status)
    except Exception as e:
        logger.error(f"Error checking Gmail connection status: {str(e)}")
        return jsonify({
            'connected': False,
            'error': str(e)
        }), 500

@gmail_bp.route('/disconnect', methods=['POST'])
def disconnect():
    """
    Disconnects a client's Gmail account.
    
    Request Body:
        client_id: The client ID
    
    Returns:
        JSON with success status
    """
    try:
        # Parse request body
        data = request.get_json()
        client_id = data.get('client_id')
        
        if not client_id:
            return jsonify({
                'success': False,
                'error': 'Client ID is required'
            }), 400
        
        success = disconnect_gmail(client_id)
        
        return jsonify({
            'success': success,
            'message': 'Gmail disconnected successfully' if success else 'Failed to disconnect Gmail'
        })
    except Exception as e:
        logger.error(f"Error disconnecting Gmail: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@gmail_bp.route('/send', methods=['POST'])
def send():
    """
    Sends an email using a client's Gmail account.
    
    Request Body:
        client_id: The client ID
        to: Recipient email address
        subject: Email subject
        body: Email body (HTML format)
        cc: CC recipients (optional)
        bcc: BCC recipients (optional)
    
    Returns:
        JSON with success status and thread/message IDs if successful
    """
    try:
        # Parse request body
        data = request.get_json()
        
        required_fields = ['client_id', 'to', 'subject', 'body']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    'success': False,
                    'error': f'Missing required field: {field}'
                }), 400
        
        # Extract fields
        client_id = data.get('client_id')
        to = data.get('to')
        subject = data.get('subject')
        body = data.get('body')
        cc = data.get('cc')
        bcc = data.get('bcc')
        
        # Send email
        result = send_email(
            client_id=client_id,
            to=to,
            subject=subject,
            body=body,
            cc=cc,
            bcc=bcc
        )
        
        if result.get('success'):
            return jsonify(result)
        else:
            return jsonify(result), 400
    except Exception as e:
        logger.error(f"Error sending email: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500 
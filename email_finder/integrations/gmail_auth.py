"""
Gmail Authentication Module for Email Finder System.

This module provides functions for authenticating users with Gmail using OAuth2.
It stores authentication tokens in Firebase Firestore.
"""

import os
import json
import logging
from typing import Dict, Any, Optional, Tuple
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from email_finder.storage.firebase import get_firestore_client

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Gmail API scopes
GMAIL_SCOPES = [
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/gmail.readonly'
]

def get_oauth2_flow(redirect_uri: str) -> Flow:
    """
    Creates an OAuth2 flow for Gmail authentication.
    
    Args:
        redirect_uri: The URI to redirect to after authentication
    
    Returns:
        Flow: The OAuth2 flow object
    """
    try:
        client_config = {
            "web": {
                "client_id": os.environ.get("GOOGLE_CLIENT_ID"),
                "client_secret": os.environ.get("GOOGLE_CLIENT_SECRET"),
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "redirect_uris": [redirect_uri]
            }
        }
        
        # Create flow instance to manage the OAuth 2.0 Authorization Grant Flow steps
        flow = Flow.from_client_config(
            client_config=client_config,
            scopes=GMAIL_SCOPES
        )
        flow.redirect_uri = redirect_uri
        
        return flow
    except Exception as e:
        logger.error(f"Error creating OAuth2 flow: {str(e)}")
        raise

def store_tokens(client_id: str, tokens: Dict[str, Any]) -> bool:
    """
    Stores Gmail auth tokens in Firestore.
    
    Args:
        client_id: The client ID to associate with the tokens
        tokens: The OAuth2 tokens to store
    
    Returns:
        bool: Success status
    """
    try:
        db = get_firestore_client()
        
        # Store tokens in Firestore
        doc_ref = db.collection('clients').document(client_id)
        
        # Get current data to preserve other fields
        doc = doc_ref.get()
        if doc.exists:
            current_data = doc.to_dict()
        else:
            current_data = {}
        
        # Update with Gmail tokens
        current_data.update({
            'gmailAccessToken': tokens.get('access_token'),
            'gmailRefreshToken': tokens.get('refresh_token'),
            'gmailTokenExpiry': tokens.get('expiry'),
            'updatedAt': firestore.SERVER_TIMESTAMP
        })
        
        # Write to Firestore
        doc_ref.set(current_data)
        
        logger.info(f"Gmail tokens stored for client {client_id}")
        return True
    except Exception as e:
        logger.error(f"Error storing Gmail tokens: {str(e)}")
        return False

def get_tokens(client_id: str) -> Optional[Dict[str, Any]]:
    """
    Retrieves Gmail auth tokens from Firestore.
    
    Args:
        client_id: The client ID
    
    Returns:
        Optional[Dict[str, Any]]: The OAuth2 tokens if found, None otherwise
    """
    try:
        db = get_firestore_client()
        
        # Get client data from Firestore
        doc_ref = db.collection('clients').document(client_id)
        doc = doc_ref.get()
        
        if not doc.exists:
            logger.warning(f"No client found with ID {client_id}")
            return None
        
        client_data = doc.to_dict()
        
        # Check if Gmail tokens exist
        if not client_data.get('gmailAccessToken'):
            logger.warning(f"Client {client_id} has no Gmail access token")
            return None
        
        # Return tokens
        return {
            'access_token': client_data.get('gmailAccessToken'),
            'refresh_token': client_data.get('gmailRefreshToken'),
            'expiry': client_data.get('gmailTokenExpiry')
        }
    except Exception as e:
        logger.error(f"Error retrieving Gmail tokens: {str(e)}")
        return None

def get_gmail_client(client_id: str) -> Optional[Any]:
    """
    Gets an authorized Gmail client for a client.
    
    Args:
        client_id: The client ID
    
    Returns:
        Optional[Any]: A configured Gmail client or None if authentication fails
    """
    try:
        # Get tokens from Firestore
        tokens = get_tokens(client_id)
        
        if not tokens:
            logger.warning(f"No Gmail tokens found for client {client_id}")
            return None
        
        # Create credentials from tokens
        credentials = Credentials(
            token=tokens.get('access_token'),
            refresh_token=tokens.get('refresh_token'),
            token_uri="https://oauth2.googleapis.com/token",
            client_id=os.environ.get("GOOGLE_CLIENT_ID"),
            client_secret=os.environ.get("GOOGLE_CLIENT_SECRET"),
            scopes=GMAIL_SCOPES
        )
        
        # Build Gmail client
        gmail = build('gmail', 'v1', credentials=credentials)
        
        return gmail
    except Exception as e:
        logger.error(f"Error getting Gmail client: {str(e)}")
        return None

def verify_gmail_connection(client_id: str) -> Dict[str, Any]:
    """
    Verifies connection to Gmail and returns status.
    
    Args:
        client_id: The client ID
    
    Returns:
        Dict[str, Any]: Connection status information
    """
    try:
        gmail = get_gmail_client(client_id)
        
        if not gmail:
            return {'connected': False, 'error': 'No Gmail client available'}
        
        # Test connection by getting user profile
        profile = gmail.users().getProfile(userId='me').execute()
        
        return {
            'connected': True,
            'email': profile.get('emailAddress'),
            'scopes': GMAIL_SCOPES
        }
    except HttpError as e:
        error_content = json.loads(e.content.decode())
        error_message = error_content.get('error', {}).get('message', str(e))
        
        logger.error(f"Gmail API error: {error_message}")
        return {'connected': False, 'error': error_message}
    except Exception as e:
        logger.error(f"Error verifying Gmail connection: {str(e)}")
        return {'connected': False, 'error': str(e)}

def disconnect_gmail(client_id: str) -> bool:
    """
    Disconnects Gmail integration for a client.
    
    Args:
        client_id: The client ID
    
    Returns:
        bool: Success status
    """
    try:
        db = get_firestore_client()
        
        # Get client data
        doc_ref = db.collection('clients').document(client_id)
        doc = doc_ref.get()
        
        if not doc.exists:
            logger.warning(f"No client found with ID {client_id}")
            return False
        
        # Update to remove Gmail tokens
        doc_ref.update({
            'gmailAccessToken': None,
            'gmailRefreshToken': None,
            'gmailTokenExpiry': None,
            'updatedAt': firestore.SERVER_TIMESTAMP
        })
        
        logger.info(f"Gmail disconnected for client {client_id}")
        return True
    except Exception as e:
        logger.error(f"Error disconnecting Gmail: {str(e)}")
        return False

def send_email(
    client_id: str,
    to: str,
    subject: str,
    body: str,
    cc: Optional[str] = None,
    bcc: Optional[str] = None
) -> Dict[str, Any]:
    """
    Sends an email using Gmail.
    
    Args:
        client_id: The client ID
        to: Recipient email address
        subject: Email subject
        body: Email body (HTML format)
        cc: CC recipients (optional)
        bcc: BCC recipients (optional)
    
    Returns:
        Dict[str, Any]: Result with success status and message/thread IDs if successful
    """
    try:
        gmail = get_gmail_client(client_id)
        
        if not gmail:
            return {
                'success': False,
                'error': 'No Gmail client available. Please connect Gmail first.'
            }
        
        # Construct email headers
        headers = [
            f'To: {to}',
            f'Subject: {subject}',
            'Content-Type: text/html; charset=utf-8',
            'MIME-Version: 1.0'
        ]
        
        # Add CC and BCC if provided
        if cc:
            headers.append(f'Cc: {cc}')
        if bcc:
            headers.append(f'Bcc: {bcc}')
        
        # Construct full email
        email_lines = headers + ['', body]
        email_content = '\r\n'.join(email_lines)
        
        # Encode as base64url (Gmail API requirement)
        from base64 import urlsafe_b64encode
        encoded_email = urlsafe_b64encode(email_content.encode()).decode()
        
        # Send the email
        logger.info(f"Sending email to {to}")
        response = gmail.users().messages().send(
            userId='me',
            body={'raw': encoded_email}
        ).execute()
        
        # Extract IDs from response
        thread_id = response.get('threadId', '')
        message_id = response.get('id', '')
        
        logger.info(f"Email sent successfully. Thread ID: {thread_id}, Message ID: {message_id}")
        
        return {
            'success': True,
            'threadId': thread_id,
            'messageId': message_id
        }
    except HttpError as e:
        error_content = json.loads(e.content.decode())
        error_message = error_content.get('error', {}).get('message', str(e))
        
        logger.error(f"Gmail API error: {error_message}")
        return {'success': False, 'error': error_message}
    except Exception as e:
        logger.error(f"Error sending email: {str(e)}")
        return {'success': False, 'error': str(e)}

# Import necessary Firebase modules here to avoid circular imports
from firebase_admin import firestore 
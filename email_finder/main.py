"""
Main application file for the Email Finder System.

This file initializes the Flask app and registers all blueprints.
"""

import os
import logging
from flask import Flask, render_template

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__, 
                template_folder='dashboard/templates',
                static_folder='dashboard/static')
    
    # Configure app
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'dev_key'),
        DEBUG=os.environ.get('FLASK_DEBUG', 'False') == 'True'
    )
    
    # Register Gmail endpoints
    from email_finder.api.gmail_endpoints import gmail_bp
    app.register_blueprint(gmail_bp)
    
    # Define routes
    @app.route('/')
    def index():
        """Render the home page."""
        return render_template('index.html')
    
    @app.route('/dashboard')
    def dashboard():
        """Render the dashboard page."""
        return render_template('dashboard.html')
    
    @app.errorhandler(404)
    def page_not_found(e):
        """Handle 404 errors."""
        return render_template('404.html'), 404
    
    @app.errorhandler(500)
    def server_error(e):
        """Handle 500 errors."""
        logger.error(f"Server error: {str(e)}")
        return render_template('500.html'), 500
    
    return app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 
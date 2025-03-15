# Email Finder System

A production-ready, scalable, AI-powered platform that autonomously finds contact emails for target individuals and companies through a three-tiered approach:
1. Brave Search API
2. Website scraping with ZenRows
3. Browser-based form submission

## Core Features

- **Multi-Client Support**: Supports 50+ different clients simultaneously, each with isolated data and customized settings
- **AI-Powered Intelligence**: Uses Claude 3.7 Sonnet via AWS Bedrock for all analysis tasks
- **Progressive Discovery**: Optimizes resource usage by progressively attempting more resource-intensive methods
- **Cross-Validation**: Validates discovered emails through multiple independent methods
- **Reputation Management**: Prevents detection as automation through human-like request patterns
- **White-Label Configuration**: Supports client-specific branding and customization
- **Gmail Integration**: Authenticate with Gmail to send personalized outreach emails directly from the platform

## Directory Structure

```
/email_finder/
  /storage/       # Firebase and data storage components
  /api/           # API clients (Claude, Brave Search, ZenRows, Gmail)
  /browser/       # Browser automation components
  /core/          # Core orchestration logic
  /upload/        # Document upload and processing
  /customization/ # Client customization components
  /multi_client/  # Multi-client architecture components
  /orchestration/ # Strategy orchestration components
  /dashboard/     # Dashboard and visualization components
  /integrations/  # External integrations (Gmail, Zapier, etc.)
  /utils/         # Utility functions and helpers
```

## Getting Started

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set up environment variables:
   ```
   cp .env.example .env
   # Edit .env with your API keys and configuration
   ```

3. Set up Google OAuth credentials:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one
   - Navigate to "APIs & Services" > "Credentials"
   - Create an OAuth 2.0 Client ID (Web application)
   - Add the redirect URI: `http://localhost:5000/api/email-gmail/oauth-callback`
   - Copy the Client ID and Client Secret to your `.env` file

4. Run the web application:
   ```
   export FLASK_APP=email_finder.main
   export FLASK_ENV=development
   flask run
   ```

5. Run the CLI:
   ```
   python -m scripts.email_finder_cli --help
   ```

## Gmail Integration

The Email Finder System includes a comprehensive Gmail integration to send personalized outreach emails:

1. **Authentication**: OAuth 2.0 authentication with Gmail
2. **Token Management**: Securely store and refresh OAuth tokens in Firebase
3. **Email Sending**: Send HTML emails with attachments and tracking
4. **Per-Client Configuration**: Each client has their own Gmail authentication

### Using Gmail Integration

1. Navigate to the dashboard at `http://localhost:5000/dashboard`
2. Click "Connect Gmail" in the Email Integrations section
3. Follow the Google OAuth flow to grant permissions
4. Once connected, you can send test emails from the dashboard

## Testing

Run the test suite:
```
pytest
```

Or run specific tests:
```
python -m scripts.test_email_finder --target="Acme Inc" --store-results=true
```

## Documentation

See the `docs/` directory for detailed documentation on each component. 
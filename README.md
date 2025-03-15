# Email Finder

A powerful, production-ready system that finds email addresses through multi-tiered approach, using AI to orchestrate the discovery process.

## Features

- **Multi-Client Architecture**: Support for multiple clients with isolated data
- **Progressive Discovery**: Optimizes resource usage with increasing levels of intensity
- **Gmail Integration**: Send personalized outreach emails directly from the platform
- **AI-Powered**: Uses Claude 3.7 Sonnet via AWS Bedrock for intelligent decision making
- **Cross-Validation**: Validates discovered emails through multiple verification methods

## Project Structure

The project is organized into several modules:

```
/email_finder/
  /storage/       # Data storage components
  /api/           # External API clients
  /browser/       # Browser automation components
  /core/          # Core orchestration logic
  /dashboard/     # UI components
  /integrations/  # External integrations (Gmail, etc.)
  /utils/         # Utility functions
```

## Getting Started

1. Clone the repository:
   ```
   git clone https://github.com/ReeceHarding/email-finder.git
   cd email-finder
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   ```
   cp .env.example .env
   # Edit .env with your API keys and settings
   ```

4. Run the web application:
   ```
   export FLASK_APP=email_finder.main
   flask run
   ```

## Gmail Integration

This project includes a full Gmail integration to send personalized outreach emails:

- OAuth 2.0 authentication flow
- Secure token storage in Firebase
- HTML email composition
- Per-client configuration

## License

[MIT License](LICENSE) 
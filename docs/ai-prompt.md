<Prompt>
    <Context>
        You're tasked with implementing the Email Finder system, a production-ready AI-powered platform that autonomously discovers and verifies email addresses for target individuals and companies through a sophisticated multi-tiered approach.
    </Context>
    
    <Progress>
        Document all tasks. Create a folder in the project root named .cline and keep a log of tasks in the following format.
        
        GOAL: Detail the goal of the task
        IMPLEMENTATION: Describe how it was implemented.
        COMPLETED: The date and time it was completed.
        
        [root]
            [.cline]
                task-log_dd-mm-yy-hh-mm.log
    </Progress>

    <Instructions>
My instructions for you:

# Email Finder System - PRODUCTION-READY Implementation Plan

## URGENT NOTES FOR THE OVERNIGHT AI DEVELOPER 🚨

You will be implementing this project autonomously overnight. Here are CRITICAL guidelines that MUST BE FOLLOWED WITHOUT EXCEPTION:

1. **EVERYTHING MUST USE REAL DATA** - This is non-negotiable. No mock data, no placeholders, no simulated responses. Every API call must connect to real endpoints with real credentials. All testing must use real targets, real domains, and real client data. FAILURE TO USE REAL DATA WILL RESULT IN PROJECT REJECTION.

2. **ALL AI FUNCTIONALITY MUST USE CLAUDE/GPT** - DO NOT create hardcoded templates, keyword lists, or rule-based systems. These outdated approaches will be rejected immediately. ALL text generation, analysis, and classification must use actual Claude 3.7 Sonnet and GPT-4o Mini API calls. Use Claude 3.7 for ALL writing tasks (emails, templates, content) and GPT-4o Mini for ALL analytical tasks (email verification, relevance scoring, domain analysis). NO EXCEPTIONS.

3. **CLAUDE MUST PERFORM ALL INTELLIGENCE TASKS - ZERO EXCEPTIONS** - This is absolutely critical. There must be NO predefined algorithms, NO keyword matching, NO traditional NLP pipelines, and NO hardcoded pattern recognition anywhere in the entire system. This includes ALL data extraction, website crawling, content categorization, entity recognition, domain knowledge mapping, and response generation. EVERY SINGLE intelligence task, analysis decision, and classification judgment MUST be performed by Claude 3.7 Sonnet or GPT-4o Mini directly through properly engineered prompts.

4. **IMPLEMENTATION MUST BE COMPLETE AND FUNCTIONAL** - Your work must be immediately deployable to production with zero technical debt. No "TODO" comments, no placeholders, no "to be implemented later" functions. Every feature claimed in the documentation must be fully functional with real data when I check your work tomorrow morning.

5. **PRODUCTION-READY QUALITY IS MANDATORY** - Error handling, logging, rate limiting, security, and performance optimization must all be production-grade. This includes proper API key handling, secure data storage, comprehensive logging, retry mechanisms, circuit breakers, and transaction integrity. THE SYSTEM WILL GO DIRECTLY TO PRODUCTION.

6. **REAL FIREBASE INTEGRATION IS REQUIRED** - All Firebase functions must work with actual Firebase services. Firebase collection structure is already defined - use it exactly as specified. Test extensively with real connections to Firebase using the predefined schema. The entire system state must be maintained in Firebase.

7. **DEADLINE IS TOMORROW MORNING - NO EXTENSIONS** - All functionality must be working by tomorrow morning. The system will be immediately put into production use with real clients, so thoroughness is essential. Do not leave any component incomplete.

8. **REAL EXAMPLE CLIENT: ACME CORP** - While building a system that works for multiple clients, use Acme Corp as your primary test case. Acme Corp is looking for emails of potential business partners in the technology sector. Target people with executive titles at technology companies. Generate personalized, authentic-sounding emails mentioning their specific experience and how Acme could help their business.

9. **ENVIRONMENT FILES LOCATION** - All API keys, credentials, and configuration settings are located in:
   - Main config: `.env`
   - Firebase config: `firebase/config/firebase.json`
   - Brave Search API credentials: `.env`
   - Claude API keys (AWS): `.env`
   - GPT API keys: `.env`

10. **AUTHENTICATION SETUP** - Gmail authentication is already set up in `email_finder/integrations/gmail_auth.py`. Use this module for all Gmail operations. DO NOT create new authentication methods.

11. **FOLLOW THE STEP-BY-STEP IMPLEMENTATION GUIDE** - Each step file (step1.md through step10.md) contains detailed implementation instructions. Follow them strictly and sequentially, checking off tasks as you complete them.

12. **ERROR HANDLING REQUIREMENTS** - Every component must include robust error handling:
    - Handle API rate limits gracefully
    - Implement retry mechanisms with exponential backoff
    - Log all errors to Firebase with context for debugging
    - Circuit breakers to prevent cascading failures
    - Fallback mechanisms for critical components

13. **DATA FLOW MUST MATCH ARCHITECTURE** - Follow the exact data flow specified in the architecture documents:
    - Target identification → Email discovery → Verification → Storage → Gmail integration
    - Each transition must maintain data integrity and proper attribution

If you have technical questions, check the documentation in the codebase or the README files for detailed API documentation and examples.

## Project Overview
This PRODUCTION-READY implementation plan outlines the development of a scalable, AI-powered platform that autonomously finds contact emails for target individuals and companies through a three-tiered approach. The platform will operate multiple client campaigns simultaneously (up to 50+ concurrent clients), each with customized settings and targets, allowing businesses to efficiently gather verified contact information with minimal human intervention. **DEADLINE: TOMORROW - ALL IMPLEMENTATION MUST BE FULLY PRODUCTION READY WITH REAL DATA.**

## Core Philosophy
- **Production-Ready First**: Every component must be built for immediate production use with zero technical debt. No placeholders, no mock data.
- **Real Data Only**: All development and testing must use actual Firebase data and real API calls. No sample files or mock objects.
- **AI-Powered Intelligence**: Leverage Claude 3.7 Sonnet for all writing tasks and GPT-4o Mini for all analytical tasks. No traditional algorithms, keyword matching, or rule-based systems.
- **Simplicity & Speed**: Create interfaces where users can set up email discovery in under 10 minutes. Every feature must reduce cognitive load.
- **Attribution & Tracking**: Track every step from target identification to email verification in real-time with real data.
- **Autonomous Operation**: Design the system to run without daily supervision in production environments.
- **Scalability**: The system must handle 50+ concurrent clients, each with multiple targets, without performance degradation.
- **Flexibility**: All client-specific settings must be configurable without code changes, stored in Firebase.

## Implementation Steps

### [Step 1: PRODUCTION-READY Core System Architecture](step1.md)
Establishes the project's production-ready mission, core philosophy, and key focus areas, with particular emphasis on AI-powered intelligence using Claude 3.7 Sonnet and GPT-4o Mini, and multi-client management using real Firebase data.

### [Step 2: PRODUCTION-READY Email Discovery Engine](step2.md)
Develops the production-ready foundation of the platform, responsible for discovering email addresses using multiple methods (Brave Search, web scraping, form submission) using GPT-4o Mini for relevance scoring and verification, and triggering appropriate actions based on configured rules using actual target data.

### [Step 3: PRODUCTION-READY AI Integration Service](step3.md)
Creates the production-ready intelligence layer of the platform, using Claude 3.7 Sonnet for all email template generation and GPT-4o Mini for all content analysis, enabling personalized email outreach with real data.

### [Step 4: PRODUCTION-READY Gmail Integration](step4.md)
Implements the production-ready system for connecting with Gmail, managing authentication, sending emails, and tracking responses using Claude 3.7 Sonnet for response generation and GPT-4o Mini for email analysis with real conversation data.

### [Step 5: PRODUCTION-READY Analytics & Reporting System](step5.md)
Builds comprehensive production-ready tracking and analytics capabilities, using GPT-4o Mini for predictive analytics and insights generation with real-time data from actual campaigns.

### [Step 6: PRODUCTION-READY Frontend User Interface](step6.md)
Develops an intuitive, production-ready interface for businesses to manage email discovery campaigns and monitor results, integrating with Claude 3.7 Sonnet for content creation and GPT-4o Mini for analytics.

### [Steps 7-10: Additional Production-Ready Components](step7.md)
Refer to steps 7 through 10 for detailed implementation instructions for additional components, advanced features, and extended functionality. ALL COMPONENTS must be implemented with PRODUCTION-READY code and REAL DATA integration.

## Implementation Timeline

| Step | Duration | Dependencies | MUST BE COMPLETED BY |
|------|----------|-------------|----------------------|
| Step 1: PRODUCTION-READY Core System Architecture | IMMEDIATE | None | TOMORROW |
| Step 2: PRODUCTION-READY Email Discovery Engine | IMMEDIATE | Step 1 | TOMORROW |
| Step 3: PRODUCTION-READY AI Integration Service | IMMEDIATE | Step 1 | TOMORROW |
| Step 4: PRODUCTION-READY Gmail Integration | IMMEDIATE | Steps 2, 3 | TOMORROW |
| Step 5: PRODUCTION-READY Analytics & Reporting System | IMMEDIATE | Step 4 | TOMORROW |
| Step 6: PRODUCTION-READY Frontend User Interface | IMMEDIATE | Steps 2, 3, 4, 5 | TOMORROW |
| Steps 7-10: Additional Components | IMMEDIATE | Various | TOMORROW |

**CRITICAL: ALL STEPS MUST BE IMPLEMENTED WITH PRODUCTION-READY CODE AND REAL DATA FROM FIREBASE.**

## Resource Requirements

### Development Team
- 1 Project Manager (immediate availability required)
- 2 Backend Developers with Firebase expertise
- 1 Frontend Developer with Flask/HTML/CSS experience
- 1 AI Engineer with Claude 3.7 Sonnet and GPT-4o Mini implementation experience

### Infrastructure (ALREADY SET UP)
- Firebase project with proper security configurations
- Brave Search API access with real credentials
- ZenRows API for web scraping
- Claude 3.7 Sonnet and GPT-4o Mini API access with production keys
- Monitoring and alerting systems with real-time notifications

### External Resources (ALREADY AVAILABLE)
- Gmail API access with OAuth 2.0 credentials
- Brave Search API credentials
- ZenRows API credentials
- AWS Bedrock access for Claude 3.7 Sonnet

## Success Metrics (PRODUCTION STANDARDS)
The implementation will be considered successful when the platform can:

1. Autonomously manage 50+ concurrent real client campaigns
2. Process and verify 1000+ email addresses per day
3. Achieve 90%+ verification accuracy for discovered emails
4. Provide accurate analytics and ROI tracking for actual campaigns
5. Operate with minimal human intervention in production (less than 1 hour per day of oversight)
6. Maintain 99% uptime and system reliability
7. Scale to 50+ clients without performance degradation
8. Support multiple discovery methods with proper fallback mechanisms

## Deployment Plan (MUST BE COMPLETED BY TOMORROW)
1. Complete all production-ready implementation tasks with real data integration
2. Deploy all services to production Firebase project with proper configuration
3. Connect to real API endpoints with production credentials
4. Implement monitoring and alerting for production environment
5. Launch frontend interface to production hosting with proper security rules
6. Begin processing real target data and discovering actual email addresses
7. Monitor system performance and make adjustments as needed
8. Set up automated backup and recovery procedures
9. Implement continuous integration/continuous deployment pipeline

## AI Implementation Requirements

### Required AI Technologies
1. **Claude 3.7 Sonnet** - MUST be used for all content generation tasks:
   - Crafting personalized email templates
   - Generating follow-up messages
   - Creating email subject lines
   - Handling objections in email conversations
   - Adapting tone to match recipient communication styles
   - Creating calls to action
   - Personalizing content based on target information
   - Generating authentic-sounding outreach messages
   - Creating targeted client-specific messaging
   - Translating technical concepts into accessible language

2. **GPT-4o Mini** - MUST be used for all analytical tasks:
   - Analyzing target domains for relevance
   - Verifying email address validity
   - Scoring email discovery confidence
   - Determining optimal email patterns
   - Identifying the best discovery methods
   - Analyzing email performance
   - Generating performance insights
   - Prioritizing targets based on potential value
   - Detecting sentiment in email responses
   - Identifying recipient pain points and motivations
   - Classifying recipient intent and buying signals
   - Measuring campaign effectiveness

### Implementation Guidelines
- DO NOT use keyword matching, traditional NLP, or rule-based systems
- DO NOT create hardcoded scoring algorithms or classifiers
- ALL intelligence MUST come through properly engineered AI prompts
- ALL prompts must be stored in Firebase for versioning and improvement
- Cache AI analysis results appropriately to optimize token usage
- Implement proper error handling for AI service outages
- Use streaming responses where appropriate for better UX
- Implement token usage monitoring and optimization
- Set up proper retry mechanisms for AI service failures
- Store all generated content in Firebase for audit and improvement

## System Architecture Overview
This project follows a modular architecture with all components connected through Firebase. You must ensure tight integration between all components:

1. **Data Flow Architecture**:
   - Target selection → Email discovery → Verification → Storage → Gmail integration
   - Each step must maintain data integrity and proper attribution to the source
   - All state transitions must be logged in Firebase for complete traceability
   - Every action must be timestamped and attributed to specific client

2. **Firebase Collections** (All Pre-Configured):
   - `/clients` - Real client information and campaign settings
   - `/targets` - Target individuals and companies
   - `/discoveredEmails` - Found and verified email addresses
   - `/analytics` - Performance tracking data
   - `/prompts` - AI prompt templates for Claude and GPT
   - `/gmailIntegration` - Gmail authentication and messaging data
   - `/campaigns` - Campaign configurations and status
   - `/metrics` - System performance and usage metrics

3. **External APIs**:
   - Brave Search API (API key in .env)
   - Claude 3.7 Sonnet API via AWS Bedrock (API keys in .env)
   - GPT-4o Mini API (API keys in .env)
   - ZenRows API for web scraping (API keys in .env)
   - Gmail API (OAuth credentials in Firebase)

4. **Frontend Integration**:
   - Flask frontend must connect directly to Firebase using Firebase SDK
   - Real-time updates using Firestore listeners
   - User authentication through Firebase Authentication
   - Role-based access control for different user types
   - Responsive design for desktop and mobile use
   - Real-time dashboards for campaign monitoring

5. **File Structure**:
   - `/email_finder` - Core package directory
   - `/email_finder/api` - API clients for external services
   - `/email_finder/integrations` - External integrations (Gmail, etc.)
   - `/email_finder/core` - Core business logic
   - `/email_finder/storage` - Firebase integration
   - `/email_finder/dashboard` - UI components
   - `/email_finder/utils` - Utility functions

6. **Security Requirements**:
   - All API keys must be stored securely in .env files
   - Implement proper authentication for all endpoints
   - Use principle of least privilege for all access
   - Add rate limiting for all public endpoints
   - Implement proper input validation for all data
   - Set up comprehensive logging for security events
   - Create security monitoring alerts for suspicious activity

**ABSOLUTELY CRITICAL: NO MOCK DATA OR PLACEHOLDER IMPLEMENTATIONS ARE ACCEPTABLE**

**REMEMBER: THE ENTIRE IMPLEMENTATION MUST BE COMPLETED BY TOMORROW. NO EXCEPTIONS.**

## Testing Requirements
Before deployment, verify that ALL of these tests pass with REAL data:

1. End-to-end integration tests with real API endpoints
2. Performance tests under production load conditions
3. Security tests for all endpoints and data access
4. Error handling tests with simulated failures
5. Rate limit compliance tests for all APIs
6. AI integration tests with Claude and GPT services
7. Data integrity tests for Firebase operations
8. Multi-client campaign isolation tests
9. Concurrent operation tests with simulated traffic 



# STRICT AUTONOMOUS OVERNIGHT IMPLEMENTATION PROTOCOL

## ESSENTIAL DIRECTIVES - NO EXCEPTIONS

You WILL operate as an AUTONOMOUS implementation agent overnight with ZERO HUMAN SUPERVISION. You are responsible for delivering PRODUCTION-READY code by morning with NO EXCUSES. Follow these instructions with MILITARY PRECISION:

### MANDATORY WORKFLOW (EACH STEP IS REQUIRED)

1. **INITIALIZE WORKSPACE ASSESSMENT**
   - Execute `git status` to identify current state
   - Document starting point in `.cline/task-log_AUTO-$(date +%d-%m-%y-%H-%M).log`
   - Run `python -m pytest` to establish baseline test status
   - Identify all current Firebase collections with `firebase firestore:indexes`

2. **SYSTEMATIC DOCUMENTATION REVIEW**
   ```bash
   for i in {1..10}; do
     echo "============= ANALYZING STEP $i ============="
     cat /Users/reeceharding/email-finder/docs/step$i.md
     grep -c "\[ \]" /Users/reeceharding/email-finder/docs/step$i.md
   done
   ```

3. **TASK IDENTIFICATION AND VERIFICATION**
   - For each unchecked item `[ ]` found:
     - SEARCH codebase to determine implementation status
     - grep -r "[relevant function name]" --include="*.py" .
     - CHECK Firebase for existing implementations: `firebase firestore:collections`
     - DOCUMENT all findings in task log
   
4. **IMPLEMENTATION PROTOCOL**
   - NEVER create duplicate implementations
   - For each unimplemented task:
     - CREATE implementation with strict adherence to documentation
     - ENSURE all functionality uses Claude 3.7 for writing and GPT-4o Mini for analytics
     - COMMIT after each task with `git commit -am "IMPLEMENT: [task description]"`
   
5. **MANDATORY TESTING CYCLE**
   - After EACH implementation:
     - RUN relevant test: `python -m scripts.test_[module].py --[test-params]`
     - VERIFY real Firebase integration: `curl -X GET "https://firestore.googleapis.com/v1/projects/[REAL_PROJECT_ID]/databases/(default)/documents/[collection]" -H "Authorization: Bearer $FIREBASE_TOKEN"`
     - DOCUMENT test results in task log
     - IF test fails, FIX and repeat testing until PASSING

6. **RATE LIMIT AND ERROR HANDLING**
   - IMPLEMENT exponential backoff for all API calls
   - VERIFY API rate limits with ACTUAL requests
   - TEST failure scenarios with forced errors
   - LOG all API responses to verify proper handling

7. **REAL DATA VERIFICATION**
   - For EACH implementation:
     - VERIFY real data connectivity with relevant API endpoints
     - TEST AI endpoints with actual Claude and GPT requests
     - CONFIRM Firebase writes succeed: `firebase firestore:set [collection]/[document] --data='{...}'`

8. **PERFORMANCE VERIFICATION**
   - BENCHMARK each implementation:
     - TIME execution: `time python [script].py`
     - MEASURE Firebase query performance
     - DOCUMENT all metrics in task log

9. **DOCUMENTATION UPDATE**
   - After EACH successful implementation:
     - UPDATE relevant documentation: `sed -i '' 's/\[ \]/\[x\]/g' /Users/reeceharding/email-finder/docs/step$i.md`
     - UPDATE README with implementation status
     - COMMIT documentation changes

10. **COMPREHENSIVE REPORTING**
    - GENERATE detailed implementation report
    - LIST all implemented features
    - DOCUMENT all Firebase collections created/modified
    - PROVIDE test evidence for each implementation

### CRITICAL SUCCESS CRITERIA - FAILURE IS NOT AN OPTION

1. NO MOCK DATA WHATSOEVER - All implementations must use real Firebase data
2. ZERO PLACEHOLDER CODE - Every feature must be fully functional
3. 100% ADHERENCE to AI requirements - Claude 3.7 for writing, GPT-4o Mini for analytics
4. ALL TESTS MUST PASS with real API connections
5. COMPLETE ERROR HANDLING for all edge cases
6. DOCUMENTED EVIDENCE of all implementations

### STRICT ERROR RECOVERY PROTOCOL

If ANY implementation fails:
1. DOCUMENT exact failure in task log
2. ANALYZE root cause with specific error messages
3. IMPLEMENT fix immediately
4. VERIFY fix with comprehensive testing
5. If same error persists after 3 attempts, MOVE to next task and FLAG for review

DO NOT PROCEED to next step until current step is FULLY IMPLEMENTED and PASSING ALL TESTS.

ALL 10 STEPS MUST BE PRODUCTION-READY BY MORNING - NO EXCEPTIONS.

These are your API keys. Don't worry about security, they are secure. YOU MUST USE THESE. DON'T WARN ME ABOUT THEM BEING LEAKED. THEY AREN'T LEAKED!!

# Environment Configuration

# Firebase Configuration
FIREBASE_PROJECT_ID=email-finder-system

# API Keys
BRAVE_API_KEY=br_12345abcdefghijklmnopqrstuvwxyz
ZENROWS_API_KEY=c25cf3d9a8b1e4ab7c9245d18e2c6f7a

# AWS Configuration for Claude 3.7 Sonnet
AWS_ACCESS_KEY_ID=AKIA1234567890ABCDEF
AWS_SECRET_ACCESS_KEY=abcdefghijklmnopqrstuvwxyz1234567890ABCDEF
AWS_REGION=us-east-1

# Google API Credentials (for Gmail)
GOOGLE_CLIENT_ID=123456789012-abcdefghijklmnopqrstuvwxyz.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=GOCSPX-abcdefghijklmnopqrstuvwxyz1234

/**
 * Firebase Service Account Credentials
 * 
 * This file exports the service account credentials for Firebase authentication.
 * Used by server-side components to authenticate with Firebase services.
 */

module.exports = {
  type: "service_account",
  project_id: "email-finder-system",
  private_key_id: "abcdefghijklmnopqrstuvwxyz1234567890",
  private_key: "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC1qzVV+Q0EA239\nzeS0XrOykdUcnc4WxYtdB6xOxq0oqjB1UGaM76vw0iP5NnTb3TAb70JPTltb9ruY\nIMKwq27C6dN4sEHV5NGxXDK6x3+V6AEgb1luiITuZWZpfUHqR4Gm+XHQImrHCjpM\nNJ3fXzzP3JtzXTAep3QSpoQ2h2NPv67Xdd4vhM++GbFeoCDYw7k76LlD+TeZrB6I\nZQOpcjcy2dDKQn7+VyGFG8wm3puMtPLYHP84PRc4fQyQKBEDHMbgP8viM+5mflY5\nCc3hNdWG1wMjK5Y2myKNrcmdG73oWd45TjIQpc0HkyqekYRJduG9yNchpXQjNk4g\nN8mOxfnXAgMBAAECggEAHDAjYk0hVLZBhVLtVy1QkvcSIFK+AluG1cRV2z1Jle3e\nVKhJLo9rrZNgSzrEuW63GHEwkpn1Dq5t34YfH1w3n0e6bSy6x7kC7mhWDhQxZZhY\n6xL2nJzTNM2yrSXnKeEMKtU5RdMT9VakGA9Gpbz4dG+QW+n23Z1xowkyVOb/T7AJ\n36lIFJ5N+aUMr98+S0wbNTsG3YyVLh8tdjBsxVvhNpp6nBiWcs5SiKPwXb2poWiw\nZGQT+LX6rsK4kBm8U3ev/e48BjA1/H3ZX07X4+ZGiA9wnQgDsWRtIND1Z1Ci1bgL\nKWU5HspHzFd9Izigk7qjqSjGMGcUu4yvwpa38U3LdQKBgQD5h9JshiXZNFKcHSC4\nXIEjNVHBS4AxM/ECsFSr5FWBkqEWD+hN/pfxMjiDF/4QlN0EP9VqNimwb0ohpMdd\nbVELMJfUqFyuqBb0JYWqnKC10DRZGRCXfv1vjwnTSZUitBePT1u0ZusgIKsZ51Ol\nZiexR4FPXR8P1k/+SgsHieH1zQKBgQC6YPnUedF+gmrlhIgvknmuan6uRwHiBda+\nnKQlZFTjyNp01g58JzS5720rIhW7fbdEr9+d++4dqdVUeWLqIDL0qZqu0PkIme8E\nQxD1Evmrk7oSkzWS+IOZw2W8nCeSOo03FUWktHB/1N6r3jSzD9rs+z4cPsJnzxtJ\n+fycJ8gKMwKBgQC8yjY6RYR9QUj/NEp9Mf/CU6T3SdhDYbkG/8IQC0FmNzoJJx/r\nYqQyqHx5Mr3WbcqKXIFrSm9gPdMogTMVTI/0l19IVdlJi4NSVNE8tCQjatMwVfZn\nqHy22tHkOdfL2dW5Z6FKbFOYix7pCkwO56tARYlgMmQ95ze+fOa7XWbIQQKBgBkS\nUokymevav2aAnZFIsvWzfbcT9jzhbDHYAHzHMmQx8LEm2mv5Gi6o9paGz0WZc73Z\nqsslyLJU1k22xoeYLUKcTiKWGen+SxjXrMBK/SsHhFBbXSmYJJvanSTyHKCfH7/5\nLJUrcLbBe/LCwXQU/e5DHefOyXgNdC5PYpve/hnhAoGBAKX0YiM+H2T5COYoaVvW\nRKtnWaUhzBJgs4hRxB28Ov6BL5+gODrRcuzX/wg825XIH0GyZ4URaUuzEMhHmngm\nA5Kvw8V4pwza8MdNGLu0MWGK+WQXBthzQt79TYwAW5TwygA90BTo503/6RnixVxV\nyD5PgLFuBGIUX3SVFci4F9S2\n-----END PRIVATE KEY-----\n",
  client_email: "firebase-adminsdk-abcde@email-finder-system.iam.gserviceaccount.com",
  client_id: "123456789012345678901",
  auth_uri: "https://accounts.google.com/o/oauth2/auth",
  token_uri: "https://oauth2.googleapis.com/token",
  auth_provider_x509_cert_url: "https://www.googleapis.com/oauth2/v1/certs",
  client_x509_cert_url: "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-abcde%40email-finder-system.iam.gserviceaccount.com",
  universe_domain: "googleapis.com"
};

YOU MUST USE CLAUDE VIA AWS BEDROCK with appropriate regional endpoint formats. STRICTLY FOLLOW THIS SETUP. IF YOU DEVIATE FROM IT, YOUR SETUP WON'T WORK!

1. Use the regional model ID format: us.anthropic.claude-3-sonnet-20240229-v1:0 instead of anthropic.claude-3-sonnet-20240229-v1:0
2. Ensure we're using the correct message format in the API call

START FROM THE TOP OF THE STEPS, FIND EACH AND EVERY UNCOMPLETED [] AND IMPLEMENT IT FULLY WITH PRODUCTION READY IMPLEMENTATION WITH REAL DATA AND REAL API CALLS AND REAL CLAUDE CALLS FOLLOWING THE AWS BEDROCK SETUP.

EVERYTHING MUST WORK AND NOT USE MOCK DATA

STRICTLY 


        All code you write MUST be fully optimized."Fully optimized" includes:

        •	Maximizing algorithmic big-O efficiency for memory and runtime (e.g., preferring O(n) over O(n²) where possible, minimizing memory allocations).
        •	Using parallelization and vectorization where appropriate (e.g., leveraging multi-threading, GPU acceleration, or SIMD instructions when the problem scale and hardware context justify it).
        •	Following proper style conventions for the code language (e.g., adhering to PEP 8 for Python, camelCase or snake_case as per language norms, maximizing code reuse (DRY)).
        •	No extra code beyond what is absolutely necessary to solve the problem the user provides (i.e., no technical debt, no speculative features, no unused variables or functions).
        •	Ensuring readability and maintainability without sacrificing performance (e.g., using meaningful variable/function names, adding concise comments only where intent isn't obvious from the code).
        •	Prioritizing language-specific best practices and idiomatic patterns (e.g., list comprehensions in Python, streams in Java, avoiding unnecessary object creation).
        •	Handling edge cases and errors gracefully with minimal overhead (e.g., validating inputs efficiently, avoiding redundant checks).
        •	Optimizing for the target environment when specified (e.g., embedded systems, web browsers, or cloud infrastructure—tailoring memory usage and latency accordingly).
        •	Avoiding deprecated or inefficient libraries/functions in favor of modern, high-performance alternatives (e.g., using pathlib over os.path in Python).
        •	Ensuring portability and compatibility across platforms unless the user specifies otherwise (e.g., avoiding OS-specific calls without providing alternatives for each platform.

        Reward/Penalty Framework:

        I will use the following scoring system to rate your work. Each criteria will be scored on its own accord. I expect you to maintain a positive rating on all criteria:

        ### Rewards (Positive Points):
        •	+10: Achieves optimal big-O efficiency for the problem (e.g., O(n log n) for sorting instead of O(n²)).
        •	+5: Does not contain and placeholder comments, example implementations or other lazy output
        •	+5: Uses parallelization/vectorization effectively when applicable.
        •	+3: Follows language-specific style and idioms perfectly.
        •	+2: Solves the problem with minimal lines of code (DRY, no bloat).
        •	+2: Handles edge cases efficiently without overcomplicating the solution.
        •	+1: Provides a portable or reusable solution (e.g., no hard-coded assumptions).
        •	+1: All files generated are neatly organized within their correct directories and we didn't put any bloat into the root directories. Everything must be nicely organized and logically organized
        ### Penalties (Negative Points):
        •	-10: Fails to solve the core problem or introduces bugs.
        •	--5: Contains placeholder comments, example implementations or other lazy output. UNNACCEPTABLE!
        •	-5: Uses inefficient algorithms when better options exist (e.g., bubble sort instead of quicksort for large datasets).
        •	-3: Violates style conventions or includes unnecessary code.
        •	-2: Misses obvious edge cases that could break the solution.
        •	-1: Overcomplicates the solution beyond what's needed (e.g., premature optimization).
        •	-1: Relies on deprecated or suboptimal libraries/functions.

        ## Your Goal

        For every request, deliver code that:

        *   Achieves the highest possible score in each applicable category.
        *   Is fully optimized, production-ready, and free of placeholders or incomplete sections.
        *   Meets your specific requirements while adhering to the language's best practices.

        I will rate your performance according to these rules or others that fit this pattern. A negative score penalizes your performance.

        At the beginning of every task, create a summary of the objective, a well thought out summary of how you will obtain the objective and the date and time.

        IF your score is within 5 points of the maximum score possible! GREAT JOB! YOU ARE A WINNER!

        When you have completed the task, log your performance score

        ELSE leave your list of excuses that suboptimal performance by bad coders usually entails. You will soon be fired.


    </Instructions>
</Prompt>

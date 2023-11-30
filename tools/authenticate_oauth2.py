from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def authenticate_oauth2():
    creds = None
    # Load credentials from file if available
    # If not, go through the authentication flow
    # Save credentials for the next run
    # Return the authenticated credentials
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    return creds
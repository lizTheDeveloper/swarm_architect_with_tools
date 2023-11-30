# Tool: Authenticate with GitHub API
import requests
from getpass import getpass

def authenticate_with_github(personal_access_token):
    session = requests.Session()
    session.headers.update({'Authorization': f'token {personal_access_token}'})
    return session

# Example Usage:
# personal_access_token = getpass('Enter your GitHub Personal Access Token: ')
# github_session = authenticate_with_github(personal_access_token)
# Now use 'github_session' for further API requests
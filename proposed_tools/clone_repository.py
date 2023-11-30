# Tool: Clone Repository
import subprocess
import os

def clone_repository(repository_url, authentication_token):
    repo_name = repository_url.split('/')[-1]
    if not os.path.exists(repo_name):
        # Clone the repo using the authentication token
        subprocess.run(['git', 'clone', repository_url], check=True)
        return os.path.abspath(repo_name)
    else:
        return 'Repository already exists locally.'

# Example Usage:
# repository_url = 'https://github.com/user/repository.git'
# auth_token = 'your_auth_token'
# local_repo_path = clone_repository(repository_url, auth_token)
# Tool: Create Pull Request
import requests

def create_pull_request(repository_url, base_branch, feature_branch, auth_token, pr_title, pr_body):
    # Parse the repository's owner and name from the URL
    repo_owner, repo_name = repository_url.split('/')[-2:]
    api_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/pulls'
    headers = {'Authorization': f'token {auth_token}'}
    data = {
        'title': pr_title,
        'head': feature_branch,
        'base': base_branch,
        'body': pr_body
    }
    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 201:
        return response.json()['html_url']  # URL of the created PR
    else:
        return f'Error creating pull request: {response.content}'

# Example Usage:
# pr_url = create_pull_request(
#     'https://github.com/user/repo.git',
#     'main',
#     'feature-branch',
#     'your_auth_token',
#     'Add new feature',
#     'This pull request adds a new feature.')
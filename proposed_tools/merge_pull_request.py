# Tool: Merge Pull Request
import requests


def merge_pull_request(pull_request_url, auth_token, merge_method='merge'):
    # Parse the pull request API URL
    pr_api_url = pull_request_url.replace('github.com', 'api.github.com/repos').replace('/pull/', '/pulls/')
    headers = {'Authorization': f'token {auth_token}', 'Accept': 'application/vnd.github.v3+json'}
    data = {'merge_method': merge_method}
    response = requests.put(f'{pr_api_url}/merge', headers=headers, json=data)
    if response.status_code in [200, 201]:
        return f'Pull request merged successfully with method {merge_method}.'
    else:
        return f'Error merging pull request: {response.content}'

# Example Usage:
# pr_merged = merge_pull_request(
#     'https://github.com/user/repo/pull/123',
#     'your_auth_token',
#     'squash')  # Merge method can be 'merge', 'squash', or 'rebase'
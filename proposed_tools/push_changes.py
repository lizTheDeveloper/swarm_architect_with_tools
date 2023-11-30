# Tool: Push Changes
import subprocess


def push_changes(local_repo_path, branch_name):
    # Change directory to the repository path
    original_cwd = os.getcwd()
    os.chdir(local_repo_path)
    try:
        # Push the changes to the remote branch
        subprocess.run(['git', 'push', 'origin', branch_name], check=True)
        return f'Changes pushed to {branch_name}.'
    except subprocess.CalledProcessError as e:
        return f'Error pushing changes to {branch_name}: {str(e)}'
    finally:
        # Return to the original working directory
        os.chdir(original_cwd)

# Example Usage:
# local_repo_path = '/path/to/repo'
# branch_name = 'feature-branch'
# push_result = push_changes(local_repo_path, branch_name)
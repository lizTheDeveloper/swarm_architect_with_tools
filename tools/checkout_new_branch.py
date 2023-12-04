# Tool: Checkout New Branch
import subprocess

def checkout_new_branch(local_repo_path, new_branch_name):
    # Change directory to the repository path
    original_cwd = os.getcwd()
    os.chdir(local_repo_path)
    try:
        # Fetch all branches
        subprocess.run(['git', 'fetch'], check=True)
        # Checkout new branch
        subprocess.run(['git', 'checkout', '-b', new_branch_name], check=True)
        # Return to the original working directory
        os.chdir(original_cwd)
        return f'New branch {new_branch_name} has been checked out.'
    except subprocess.CalledProcessError as e:
        # Return to the original working directory on error
        os.chdir(original_cwd)
        return f'Error checking out the branch {new_branch_name}: {str(e)}'

# Example Usage:
# local_repo_path = '/path/to/repo'
# new_branch_name = 'feature-branch'
# checkout_result = checkout_new_branch(local_repo_path, new_branch_name)
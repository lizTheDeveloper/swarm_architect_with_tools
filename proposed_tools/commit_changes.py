# Tool: Commit Changes
import subprocess

def commit_changes(local_repo_path, commit_message):
    # Change directory to the repository path
    original_cwd = os.getcwd()
    os.chdir(local_repo_path)
    try:
        # Add all changes
        subprocess.run(['git', 'add', '.'], check=True)
        # Commit the changes
        result = subprocess.run(['git', 'commit', '-m', commit_message], check=True, capture_output=True, text=True)
        return result.stdout.split()[-1]  # Extract commit hash
    except subprocess.CalledProcessError as e:
        return f'Error during commit: {str(e)}'
    finally:
        # Return to the original working directory
        os.chdir(original_cwd)

# Example Usage:
# local_repo_path = '/path/to/repo'
# commit_message = 'Added new feature'
# commit_hash = commit_changes(local_repo_path, commit_message)
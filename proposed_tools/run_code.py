# Tool: Run Repository Code
import subprocess
import os

def run_code(local_repo_path, script_to_run='run.sh'):
    # Change to the repository directory
    original_cwd = os.getcwd()
    os.chdir(local_repo_path)
    try:
        # Run the code as per the repository's instructions
        result = subprocess.run(['bash', script_to_run], capture_output=True, text=True, check=True)
        output = result.stdout
        return output
    except subprocess.CalledProcessError as e:
        return f'Error running code: {e.output}'
    finally:
        # Return to the original directory
        os.chdir(original_cwd)

# Example Usage:
# local_repo_path = '/path/to/repo'
# execution_output = run_code(local_repo_path)
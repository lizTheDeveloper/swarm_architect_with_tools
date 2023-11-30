# Python tool for executing code
import subprocess

def execute_code(code, language):
    try:
        # Define the command based on language
        if language == 'python':
            cmd = ['python', '-c', code]
        elif language == 'javascript':
            cmd = ['node', '-e', code]
        # Add more languages as needed

        # Run the command and capture output
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
        return result.stdout, result.stderr
    except subprocess.TimeoutExpired as e:
        return '', 'Execution timed out.'
    except Exception as e:
        return '', str(e)

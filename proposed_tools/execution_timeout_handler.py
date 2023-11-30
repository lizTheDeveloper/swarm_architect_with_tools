# Python tool for handling execution timeout
import signal

# Define a timeout handler
class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException

signal.signal(signal.SIGALRM, timeout_handler)

def execute_with_timeout(code, timeout_seconds, language):
    try:
        # Set the alarm
        signal.alarm(timeout_seconds)
        # Execute the code (this function should integrate with the execution logic)
        # Example: result = execute_code(code, language)
        # Cancel the alarm
        signal.alarm(0)
        return result
    except TimeoutException:
        return 'Execution timed out'
    except Exception as e:
        return str(e)

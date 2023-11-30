# Python tool for error handling and logging
import logging

# Configure logging
logging.basicConfig(filename='interpreter_error.log',
                    level=logging.ERROR,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def log_error(error_message):
    try:
        # Log the error message
        logging.error(error_message)
        return 'Logged Error: {}'.format(error_message)
    except Exception as e:
        return str(e)

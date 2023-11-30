import logging

logging.basicConfig(level=logging.ERROR)

def handle_api_error(error):
    # Extract error information
    error_msg = str(error)
    # Log the error
    logging.error(f'An error occurred: {error_msg}')
    # Return the error message
    return error_msg
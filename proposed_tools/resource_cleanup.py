# Python tool for cleaning up resources after execution
import os

def cleanup_temp_resources(resource_identifier):
    try:
        # Check if the resource is a temporary file and remove it
        if os.path.isfile(resource_identifier):
            os.remove(resource_identifier)
            return 'Temporary file cleaned up.'
        else:
            return 'No temporary file to clean up.'
    except Exception as e:
        return str(e)

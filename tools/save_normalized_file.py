# Python function to save normalized markdown files
def save_normalized_file(file_path, normalized_content):
    try:
        with open(file_path, 'w') as file:
            file.write(normalized_content)
        return 'File saved successfully.'
    except IOError as e:
        return f'An error occurred: {e}'}

tool_definition = {
    "name": "save_normalized_file",
    "description": "Save a normalized file",
    "parameters": {
        "type": "object",
        "properties": {
        "file_path": {
            "type": "string",
            "description": "The path to the file to save"
        },
        "normalized_content": {
            "type": "string",
            "description": "The normalized content to save"
        }
        },
        "required": [
        "file_path",
        "normalized_content"
        ]
    }
    }
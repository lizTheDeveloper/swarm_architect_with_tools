# Python function to read the curriculum file tree
import os
import json

def read_curriculum_tree(root_path):
    curriculum_tree = {}

    for root, dirs, files in os.walk(root_path):
        rel_path = os.path.relpath(root, root_path)
        curriculum_tree[rel_path] = [d for d in dirs] + [f for f in files if f.endswith('.md')]

    return json.dumps(curriculum_tree, indent=4)

tool_definition = {
    "name": "read_curriculum_tree",
    "description": "Read the curriculum file tree",
    "parameters": {
        "type": "object",
        "properties": {
        "root_path": {
            "type": "string",
            "description": "The root path of the curriculum file tree"
        }
        },
        "required": [
        "root_path"
        ]
    }
    }
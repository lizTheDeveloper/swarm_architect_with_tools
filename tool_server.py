from fastapi import FastAPI
import os
import importlib
import json


app = FastAPI()

## read the tools directory
tools = {}
for tool_file in os.listdir("tools"):
    tool_name = tool_file.split(".")[0]
    tool = importlib.import_module(f"tools.{tool_name}")
    tools[tool_name] = tool
    
## create a route for each tool
for tool_name, tool in tools.items():
    route_name = tool_name.replace("_", "-")
    route_function_str = f"""
@app.post(f"/{route_name}")
def {tool_name}_route(tool_input: tool.ToolInput):
    return tool.run(tool_input)
"""
    
    exec(route_function_str)
    

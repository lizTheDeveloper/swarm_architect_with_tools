# Python tool for handling input stream to a subprocess
from subprocess import Popen, PIPE, STDOUT

def provide_input_and_execute(code, input_data, language):
    try:
        # Define the process based on language
        if language == 'python':
            process = Popen(['python', '-c', code], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        elif language == 'javascript':
            process = Popen(['node', '-e', code], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        # Add more languages as needed

        # Send input and get output
        output = process.communicate(input=input_data.encode())[0]

        return output.decode()
    except Exception as e:
        return str(e)

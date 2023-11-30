# Python tool for collecting output stream of a subprocess
import subprocess

def collect_output(process):
    try:
        # Capture the output from the process
        stdout, stderr = process.communicate()
        return stdout.decode(), stderr.decode()
    except Exception as e:
        return '', str(e)

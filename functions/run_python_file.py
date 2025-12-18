import os
import subprocess
def run_python_file(working_directory,file_path,args=None): 
    try:
        path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(path,file_path))
        valid_path = os.path.commonpath([path,target_dir]) == path
        absolute_file_path = os.path.join(working_directory,file_path) 
        absolute_working_dir = os.path.abspath(working_directory)
        absolute_file_path = os.path.join(absolute_working_dir,file_path)
        if not valid_path: 
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(absolute_file_path): 
            return f'Error:"{file_path}" does not exist or is not a regular file'
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python",absolute_file_path]
        if args:
            command.extend(args)
        completed_process = subprocess.run(command, capture_output=True, text=True, timeout=30,cwd=absolute_working_dir)
        if completed_process.returncode != 0: 
            return f'Process exited with code {completed_process.returncode}'
        if not completed_process.stdout and not completed_process.stderr: 
            return "No output produced"
        parts = []
        if completed_process.stdout:
            parts.append(f"STDOUT: {completed_process.stdout}")
        if completed_process.stderr:
            parts.append(f"STDERR: {completed_process.stderr}")
        return "\n".join(parts)
    except Exception as e: 
        return f"Error: executing Python file: {e}"
        
    
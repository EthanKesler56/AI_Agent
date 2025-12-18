import os

def get_file_content(working_directory,file_path):
    path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(path,file_path))
    valid_path = os.path.commonpath([path,target_dir]) == path
    try:
        if not valid_path: 
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_dir): 
            return f'Error: File not found or is not a regular file: "{file_path}"'
     
        with open(target_dir, "r") as f: 
            content = f.read(10000)
            if f.read(1): 
                content += f'[...File "{file_path}" truncated at {10000} characters]'
            return content
    except Exception as e: 
        return f"Error: {e}"


import os

def write_file(working_directory,file_path,content): 
    path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(path,file_path))
    valid_path = os.path.commonpath([path,target_dir]) == path
    parent_dir = os.path.dirname(target_dir)
   
    try:
        if not valid_path: 
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if  os.path.isdir(target_dir): 
            return f'Error: Cannot write to "{file_path}" as it is a directory"'
      
            
        os.makedirs(parent_dir,exist_ok=True)
        with open(target_dir, "w") as f: 
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    except Exception as e: 
        return f"Error: {e}"
    
import os
def get_files_info(working_directory, directory="."):
    try:
        path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(path,directory))
        valid_path = os.path.commonpath([path,target_dir]) == path
    
        new_list = []
        if not valid_path: 
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir): 
            return f'Error: "{directory}" is not a directory'
        for item in os.listdir(target_dir): 
            full_path = os.path.join(target_dir,item)
            file_size = os.path.getsize(full_path)
            is_dir = os.path.isdir(full_path)
            line = f'- {item}: file_size={file_size} bytes, is_dir={is_dir}'
            new_list.append(line)
        return "\n".join(new_list)
    except Exception as e: 
        return f"Error: {e}"


get_files_info('/home/ethan/Workspace/AI_Agent')
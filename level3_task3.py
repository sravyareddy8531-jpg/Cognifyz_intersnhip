import os
import shutil

folder_path = r'C:/Users/Administrator/Desktop'

def organize_files():
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_extension = filename.split('.')[-1]
            
            new_folder = os.path.join(folder_path, file_extension)
            if not os.path.exists(new_folder):
                os.makedirs(new_folder)
            
            shutil.move(os.path.join(folder_path, filename), os.path.join(new_folder, filename))
            print(f"Moved: {filename} to {file_extension}/ folder")

organize_files()
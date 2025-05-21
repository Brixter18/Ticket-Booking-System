import os

file_path = 'clean_project.zip'  # or provide full path like 'F:/Project 2/moby3/clean_project.zip'
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{file_path} deleted.")
else:
    print(f"{file_path} not found.")

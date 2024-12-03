import os
import shutil
import datetime
import schedule
import time

source_dir = "C:\Users\ryanl\OneDrive\Desktop\Py Projects\PythonAutomation"
destination_dir = "C:\Users\ryanl\OneDrive\Desktop\Py Projects"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    "Backups/11-23-2023"

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")

copy_folder_to_directory(source_dir, destination_dir)
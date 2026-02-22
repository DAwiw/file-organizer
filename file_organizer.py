import os
import shutil
from datetime import datetime

BASE_DIR = os.getcwd()
INCOMING_DIR = os.path.join(BASE_DIR, "Incoming")
SORTED_DIR = os.path.join(BASE_DIR, "Sorted")

EXTENSIONS = {
    "PDF": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Docs": [".docx", ".doc", ".txt"],
    "Excel": [".xlsx", ".csv"],
    "Code": [".py", ".js", ".html", ".css"],
    "Audio": [".mp3", ".wav"],
    "Video": [".mp4", ".mov"]
}

def get_folder(ext):
    for folder, extensions in EXTENSIONS.items():
        if ext in extensions:
            return folder
    return "Others"

def organize():
    if not os.path.exists(INCOMING_DIR):
        print("Incoming folder not found.")
        return

    for filename in os.listdir(INCOMING_DIR):
        file_path = os.path.join(INCOMING_DIR, filename)

        if os.path.isfile(file_path):
            name, ext = os.path.splitext(filename.lower())

            folder_name = get_folder(ext)
            target_folder = os.path.join(SORTED_DIR, folder_name)

            os.makedirs(target_folder, exist_ok=True)

            date_str = datetime.now().strftime("%Y-%m-%d")
            new_name = f"{date_str}_{filename}"
            target_path = os.path.join(target_folder, new_name)

            if not os.path.exists(target_path):
                shutil.move(file_path, target_path)

    print("Files organized successfully!")

if __name__ == "__main__":
    organize()
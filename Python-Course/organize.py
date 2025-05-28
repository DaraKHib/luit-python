import os
import shutil
from pathlib import Path

# Define categories and their associated file extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
    "Others": []
}

def organize_desktop():
    desktop_path = Path(os.path.join(os.environ["USERPROFILE"], "Desktop"))

    for item in desktop_path.iterdir():
        if item.is_file():
            moved = False
            for category, extensions in FILE_CATEGORIES.items():
                # Loop through each extension in the category
                for extension in extensions:
                    if item.suffix.lower() == extension.lower():  # Compare file extension
                        category_folder = desktop_path / category
                        category_folder.mkdir(exist_ok=True)
                        shutil.move(str(item), category_folder / item.name)
                        moved = True
                        break
                if moved:
                    break  # Stop once the file is moved

            if not moved:
                other_folder = desktop_path / "Others"
                other_folder.mkdir(exist_ok=True)
                shutil.move(str(item), other_folder / item.name)

    print("Desktop organized successfully!")

if __name__ == "__main__":
    organize_desktop()

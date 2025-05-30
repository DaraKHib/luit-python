import os
from typing import Dict, Optional

def get_file_info_dict(path: Optional[str] = None) -> Dict[str, Dict[str, int]]:
    """
    Recursively scans the given path (or current working directory if not specified)
    and returns a dictionary where each key is the full file path and the value
    is another dictionary containing details like file size in bytes.

    Args:
        path (Optional[str]): Directory path to scan. Defaults to the current working directory.

    Returns:
        Dict[str, Dict[str, int]]: A nested dictionary where each file path maps to its metadata.
    """
    if path is None:
        path = os.getcwd()

    file_info_dict = {}

    # Recursively walk through all directories and files
    for root, _, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            file_info_dict[full_path] = {
                'size': os.path.getsize(full_path)  # Size in bytes
            }

    return file_info_dict

if __name__ == "__main__":
    # Example usage: no path provided, so it defaults to current directory
    files = get_file_info_dict()

    # Print each file's path and its corresponding info dictionary
    for path, info in files.items():
        print(f"{path}: {info}")

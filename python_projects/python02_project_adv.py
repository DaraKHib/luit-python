import os
from typing import List, Dict, Optional

def get_file_info_list(path: Optional[str] = None) -> List[Dict[str, object]]:
    """
    Recursively scans the given path (or the current working directory if not specified)
    and returns a list of dictionaries, each containing the full path and size (in bytes)
    of every file found.

    Args:
        path (Optional[str]): The directory path to scan. Defaults to current working directory.

    Returns:
        List[Dict[str, object]]: A list of dictionaries with 'path' and 'size' keys.
    """
    # Use current working directory if no path is provided
    if path is None:
        path = os.getcwd()

    file_info_list = []

    # Walk through the directory tree recursively
    for root, _, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            file_info = {
                'path': full_path,
                'size': os.path.getsize(full_path)  # Size in bytes
            }
            file_info_list.append(file_info)

    return file_info_list

if __name__ == "__main__":
    # Example usage: no path provided, defaults to current directory
    files = get_file_info_list()

    # Print each file's information
    for f in files:
        print(f)

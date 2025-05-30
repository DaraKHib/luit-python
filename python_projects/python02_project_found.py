import os
from typing import List, Dict

def get_file_info_list(directory: str) -> List[Dict[str, object]]:
    """
    Scans the given directory and returns a list of dictionaries,
    each containing the path and size (in bytes) of a file.

    Args:
        directory (str): The path to the directory to scan.

    Returns:
        List[Dict[str, object]]: A list of dictionaries with 'path' and 'size' keys.
    """
    file_info_list = []

    # Walk through items in the directory
    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)

        # Check if the item is a file
        if os.path.isfile(full_path):
            # Create a dictionary with file path and size
            file_info = {
                'path': full_path,
                'size': os.path.getsize(full_path)  # Size in bytes
            }
            file_info_list.append(file_info)

    return file_info_list

if __name__ == "__main__":
    # Get current working directory
    current_dir = os.getcwd()

    # Call the function and get the file info list
    files = get_file_info_list(current_dir)

    # Print the list of file dictionaries
    for f in files:
        print(f)
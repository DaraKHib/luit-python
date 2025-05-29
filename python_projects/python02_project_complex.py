import os

def collect_file_data(directory: str = ".") -> dict:
    """
    Recursively collects file information from the given directory.

    Args:
        directory (str): The directory to scan. Defaults to current working directory.

    Returns:
        Dict[str, Dict[str, int]]: A dictionary where each key is a file path (relative to base)
                                   and each value is a dictionary with file info (e.g., size).
    """
    file_data = {}
    base_dir = os.path.abspath(directory)

    for root, _, files in os.walk(base_dir):
        for file in files:
            full_path = os.path.join(root, file)
            relative_path = os.path.relpath(full_path, start=base_dir)
            key = os.path.join(os.path.basename(base_dir), relative_path)

            file_data[key] = {
                'size': os.path.getsize(full_path)
            }

    return file_data

if __name__ == "__main__":
    # Example usage
    files_info = collect_file_data()  # or collect_file_data("/path/to/directory")
    print(files_info)

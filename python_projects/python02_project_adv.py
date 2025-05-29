import os

def collect_file_data(directory: str = ".") -> list[dict]:
    """
    Recursively collects file information from the given directory.

    Args:
        directory (str): The directory to scan. Defaults to current working directory.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing file paths and sizes.
    """
    file_data = []
    base_dir = os.path.abspath(directory)

    for root, _, files in os.walk(base_dir):
        for file in files:
            full_path = os.path.join(root, file)
            relative_path = os.path.relpath(full_path, start=base_dir)
            file_data.append({
                'path': os.path.join(os.path.basename(base_dir), relative_path),
                'size': os.path.getsize(full_path)
            })

    return file_data

if __name__ == "__main__":
    # Example usage
    files_info = collect_file_data()  # or pass a path like collect_file_data("/some/path")
    print(files_info)
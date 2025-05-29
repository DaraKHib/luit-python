import os

def collect_file_data(directory=".") -> list[dict]:
    """
    Collects information about files in the specified directory.

    Args:
        directory (str): The directory to scan (defaults to current directory).

    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing file paths and sizes.
    """
    file_data = []
    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)
        if os.path.isfile(full_path):
            file_data.append({
                'path': full_path,
                'size': os.path.getsize(full_path)
            })
    return file_data

if __name__ == "__main__":
    files_info = collect_file_data()
    print(files_info)

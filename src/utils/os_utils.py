import os
from typing import List


def find_owl_ttl_files(root_folder: str) -> List[str]:
    """
    Find all .owl and .ttl files in the specified folder and its subfolders.

    Args:
        root_folder (str): The root directory path to search for files

    Returns:
        List[str]: A list of full paths to .owl and .ttl files
    """
    # List to store matched file paths
    matched_files: List[str] = []

    # Traverse all subdirectories using os.walk()
    for current_dir, _, files in os.walk(root_folder):
        for file in files:
            # Check file extensions (case-insensitive)
            if file.lower().endswith(('.owl', '.ttl')):
                # Get full file path and add to list
                full_path: str = os.path.join(current_dir, file)
                matched_files.append(full_path)

    return matched_files


def main() -> None:
    """
    Example usage of find_owl_ttl_files function.
    """
    # Replace with the folder path you want to search
    search_folder: str = '../../'

    # Get list of file paths
    owl_ttl_files: List[str] = find_owl_ttl_files(search_folder)

    # Print found file paths
    print("Found .owl and .ttl files:")
    for file_path in owl_ttl_files:
        print(file_path)


if __name__ == '__main__':
    main()


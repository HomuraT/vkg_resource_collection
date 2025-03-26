import csv
import os
from typing import List, Dict, Any


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



def dict_list_to_csv(dict_list: List[Dict[str, Any]], output_file: str, delimiter: str = ',') -> None:
    """
    Convert a list of dictionaries to a CSV file

    Parameters:
        dict_list: List of dictionaries, each dictionary represents a row of data
        output_file: Path to the output CSV file
        delimiter: CSV delimiter, default is comma

    Returns:
        None
    """
    if not dict_list:
        print("Dictionary list is empty, cannot generate CSV file")
        return

    # Get all keys from dictionaries as CSV column headers
    fieldnames = set()
    for d in dict_list:
        fieldnames.update(d.keys())

    # Convert to ordered list
    fieldnames = list(fieldnames)

    # Write to CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=delimiter)

        # Write column headers
        writer.writeheader()

        # Write data rows
        for row_dict in dict_list:
            writer.writerow(row_dict)

    print(f"CSV file has been successfully generated: {output_file}")

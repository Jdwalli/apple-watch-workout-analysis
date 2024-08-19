import os 
import shutil

def file_exists(file_path):
    """Checks whether a file exists at the specified path.

    This function determines if a file exists at the given path by using
    `os.path.exists`.

    Args:
        file_path (str): The path to the file whose existence is to be checked.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return bool(os.path.exists(file_path))
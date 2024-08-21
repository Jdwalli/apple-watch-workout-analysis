import os 
from config import HEALTH_EXPORT_DIRECTORIES

def file_exists(file_path) -> bool:
    """Checks whether a file exists at the specified path.

    This function determines if a file exists at the given path by using
    `os.path.exists`.

    Args:
        file_path (str): The path to the file whose existence is to be checked.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return bool(os.path.exists(file_path))

def create_health_export_directories() -> None:
    """Creates all the directories needed to house the health export data"""
    for directory in HEALTH_EXPORT_DIRECTORIES:
        os.makedirs(directory, exist_ok=True)

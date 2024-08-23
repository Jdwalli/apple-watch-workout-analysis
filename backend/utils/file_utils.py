import os 
import config

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
    for directory in config.HEALTH_EXPORT_DIRECTORIES:
        os.makedirs(directory, exist_ok=True)

def match_record_type_to_directory(record_name: str) -> str:
    if record_name in config.VITAL_SIGN_RECORDS:
        return config.HEALTH_ELEMENTS_VITALS_DIRECTORY
    if record_name in config.ACTIVITY_RECORDS:
        return config.HEALTH_ELEMENTS_ACTIVITY_DIRECTORY
    if record_name in config.AUDIO_RECORDS:
        return config.HEALTH_ELEMENTS_AUDIO_DIRECTORY
    if record_name in config.MOBILITY_RECORDS:
        return config.HEALTH_ELEMENTS_MOBILITY_DIRECTORY
    if record_name in config.ENVIRONMENTAL_RECORDS:
        return config.HEALTH_ELEMENTS_ENVIRONMENT_DIRECTORY
    if record_name in config.SLEEP_RECORDS:
        return config.HEALTH_ELEMENTS_SLEEP_DIRECTORY
    if record_name in config.SYMPTOM_RECORDS:
        return config.HEALTH_ELEMENTS_SYMPTOMS_DIRECTORY
    if record_name in config.HEALTH_RECORDS:
        return config.HEALTH_ELEMENTS_HEALTH_DIRECTORY

    print(f"{record_name} does not belong to a group!")
    return config.HEALTH_ELEMENTS_DIRECTORY

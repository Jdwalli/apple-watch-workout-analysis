import re
from config import AppleHealthPrefix


def remove_sex_prefix(input: str) -> str:
    """Removes the biological sex prefix from the input."""
    return input.removeprefix(AppleHealthPrefix.BIOLOGICAL_SEX.value)


def remove_blood_type_prefix(input: str) -> str:
    """Removes the blood type prefix from the input."""
    return input.removeprefix(AppleHealthPrefix.BLOOD_TYPE.value)


def remove_fitzpatrick_skin_type_prefix(input: str) -> str:
    """Removes the fitzpatrick skin type prefix from the input."""
    return input.removeprefix(AppleHealthPrefix.FITZPATRICK_SKIN_TYPE.value)


def remove_characteristic_type_prefix(input: str) -> str:
    """Removes the characteristic type prefix from the input."""
    return input.removeprefix(AppleHealthPrefix.CHARACTERISTIC_TYPE_IDENTIFIER.value)


def remove_category_type_prefix(input: str) -> str:
    """Removes the category type prefix from the input."""
    return input.removeprefix(AppleHealthPrefix.CATEGORY_TYPE_IDENTIFIER.value)


def remove_workout_activity_type_prefix(input: str) -> str:
    """Removes the workout activity type prefix from the input."""
    return input.removeprefix(AppleHealthPrefix.WORKOUT_ACTIVITY_TYPE.value)


def remove_workout_event_type_prefix(input: str) -> str:
    """Removes the workout event type prefix from the input."""
    return input.removeprefix(AppleHealthPrefix.WORKOUT_EVENT_TYPE.value)


def remove_quantity_type_identifier_prefix(input: str) -> str:
    """Removes the quantity type identifier prefix from the input."""
    return input.removeprefix(AppleHealthPrefix.QUANTITY_TYPE_IDENTIFIER.value)


def extract_device_name(raw_device_name: str) -> str:
    """Extracts device name using regex from a given string."""
    pattern = r"name:([^,]+)"
    return match[1] if (match := re.search(pattern, raw_device_name)) else ''


def remove_metadata_prefix(input: str) -> str:
    """Removes HK or HKMetadataKey prefix from metadata field."""
    if AppleHealthPrefix.METADATA_KEY.value in input:
        return input.removeprefix(AppleHealthPrefix.METADATA_KEY.value)
    return input.removeprefix(AppleHealthPrefix.HEALTH_KIT.value)


def determine_workout_location(input: str) -> str:
    """Determines if workout is indoor or outdoor based on value."""
    return 'Outdoor' if int(input) == 0 else 'Indoor'

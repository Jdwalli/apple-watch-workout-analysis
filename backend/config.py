from enum import Enum


class AppleHealthPrefix(Enum):
    """Enum of all the Apple Health prefixes"""
    BIOLOGICAL_SEX = "HKBiologicalSex"
    BLOOD_TYPE = "HKBloodType"
    CATEGORY_TYPE_IDENTIFIER = "HKCategoryTypeIdentifier"
    CHARACTERISTIC_TYPE_IDENTIFIER = "HKCharacteristicTypeIdentifier"
    FITZPATRICK_SKIN_TYPE = "HKFitzpatrickSkinType"
    HEALTH_KIT = "HK"
    METADATA_KEY = "HKMetadataKey"
    QUANTITY_TYPE_IDENTIFIER = "HKQuantityTypeIdentifier"
    WORKOUT_ACTIVITY_TYPE = "HKWorkoutActivityType"
    WORKOUT_EVENT_TYPE = "HKWorkoutEventType"
    
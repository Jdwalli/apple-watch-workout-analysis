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


class HeartRateMotionContext(Enum):
    """Enum of all the Heart Rate Motion Context options"""
    NOT_SET = 0
    SEDENTARY = 1
    ACTIVE = 2

    @classmethod
    def from_value(cls, value: int) -> str:
        return cls(value).name.replace('_', ' ')
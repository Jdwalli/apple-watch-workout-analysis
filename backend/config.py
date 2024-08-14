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
    """Enum of all the heart rate location options"""
    NOT_SET = 0
    SEDENTARY = 1
    ACTIVE = 2

    @classmethod
    def from_value(cls, value: int) -> str:
        return cls(value).name.replace('_', ' ')



# https://developer.apple.com/documentation/healthkit/hkworkoutswimminglocationtype
class SwimmingLocations(Enum):
    """Enum of all the swimming location options"""
    UNKNOWN = 0
    POOL = 1
    OPEN_WATER = 2

    @classmethod
    def from_value(cls, value: int) -> str:
        return cls(value).name.replace('_', ' ')


# https://developer.apple.com/documentation/healthkit/hkswimmingstrokestyle 
class SwimmingStrokeStyles(Enum):
    """Enum of all the swimming stroke styles"""
    UNKNOWN = 0
    MIXED = 1
    FREESTYLE = 2
    BACKSTROKE = 3
    BREASTSTROKE = 4
    BUTTERFLY = 5
    KICK_BOARD = 6

    @classmethod
    def from_value(cls, value: int) -> str:
        return cls(value).name.replace('_', ' ')
    

# https://developer.apple.com/documentation/healthkit/hkworkoutsessiontype
class WorkoutSessionType(Enum):
    """Enum of all the workout session types"""
    PRIMARY = 0
    MIRRORED = 1

    @classmethod
    def from_value(cls, value: int) -> str:
        return cls(value).name

# https://developer.apple.com/documentation/healthkit/hkworkoutsessionstate

# https://developer.apple.com/documentation/healthkit/hkworkouteventtype

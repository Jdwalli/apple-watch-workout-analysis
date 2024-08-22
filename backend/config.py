from enum import Enum
import os

DATA_DIRECTORY = os.path.join(os.getcwd(), "export_data")
HEALTH_ELEMENTS_DIRECTORY = os.path.join(DATA_DIRECTORY, "health_records")
ELECTROCARDIOGRAM_ELEMENTS_DIRECTORY = os.path.join(
    DATA_DIRECTORY, "electrocardiograms")
WORKOUT_ELEMENTS_DIRECTORY = os.path.join(DATA_DIRECTORY, "workout_records")
WORKOUT_ROUTE_ELEMENTS_DIRECTORY = os.path.join(
    WORKOUT_ELEMENTS_DIRECTORY, "workout-routes")

HEALTH_EXPORT_DIRECTORIES = [
    DATA_DIRECTORY,
    HEALTH_ELEMENTS_DIRECTORY,
    ELECTROCARDIOGRAM_ELEMENTS_DIRECTORY,
    WORKOUT_ELEMENTS_DIRECTORY,
    WORKOUT_ROUTE_ELEMENTS_DIRECTORY
]

ACTIVITY_SUMMARY_FILE_NAME = 'activity_summaries.csv'
WORKOUTS_SUMMARY_FILE_NAME = 'workouts.csv'


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


# https://developer.apple.com/documentation/healthkit/hkvo2maxtesttype
class VO2MaxTestType(Enum):
    """Enum of all the V02 Max Test Types"""
    MAX_EXERCISE = 1
    PREDICTION_SUB_MAX_EXERCISE = 2
    PREDICTION_NON_EXERCISE = 3

    @classmethod
    def from_value(cls, value: int) -> str:
        return cls(value).name.replace('_', ' ')


class PhysicalEffortEstimationType(Enum):
    """Enum of all the physical effort estimation types"""
    ACTIVITY_LOOKUP = 1
    DEVICE_SENSED = 2

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

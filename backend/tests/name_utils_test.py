import unittest
from utils import name_utils as name_utils


class TestNameUtils(unittest.TestCase):

    def test_remove_sex_prefix(self):
        input_value = "HKBiologicalSexMale"
        result = name_utils.remove_sex_prefix(input_value)
        expected = "Male"
        self.assertEqual(result, expected)

    def test_remove_blood_type_prefix(self):
        input_value = "HKBloodTypeaNegative"
        result = name_utils.remove_blood_type_prefix(input_value)
        expected = "aNegative"
        self.assertEqual(result, expected)

    def test_remove_fitzpatrick_skin_type_prefix(self):
        input_value = "HKFitzpatrickSkinTypeIII"
        result = name_utils.remove_fitzpatrick_skin_type_prefix(input_value)
        expected = "III"
        self.assertEqual(result, expected)

    def test_remove_characteristic_type_prefix(self):
        input_value = "HKCharacteristicTypeIdentifierdateOfBirth"
        result = name_utils.remove_characteristic_type_prefix(input_value)
        expected = "dateOfBirth"
        self.assertEqual(result, expected)

    def test_remove_category_type_prefix(self):
        input_value = "HKCategoryTypeIdentifiertoothbrushingEvent"
        result = name_utils.remove_category_type_prefix(input_value)
        expected = "toothbrushingEvent"
        self.assertEqual(result, expected)

    def test_remove_workout_activity_type_prefix(self):
        input_value = "HKWorkoutActivityTypearchery"
        result = name_utils.remove_workout_activity_type_prefix(input_value)
        expected = "archery"
        self.assertEqual(result, expected)

    def test_remove_workout_event_type_prefix(self):
        input_value = "HKWorkoutEventTypemotionResumed"
        result = name_utils.remove_workout_event_type_prefix(input_value)
        expected = "motionResumed"
        self.assertEqual(result, expected)

    def test_remove_quantity_type_identifier_prefix(self):
        input_value = "HKQuantityTypeIdentifierrunningSpeed"
        result = name_utils.remove_quantity_type_identifier_prefix(input_value)
        expected = "runningSpeed"
        self.assertEqual(result, expected)

    def test_extract_device_name(self):
        device_name = "&lt;&lt;HKDevice: 0x1234d9876&gt;, name:iPhone, manufacturer:Apple Inc., model:iPhone, hardware:iPhone11,8, software:01.0&gt;"
        result = name_utils.extract_device_name(device_name)
        expected = "iPhone"
        self.assertEqual(result, expected)
        device_name = "&lt;&lt;HKDevice: 0x2825cf520&gt;, name:Apple Watch, manufacturer:Apple Inc., model:Watch, hardware:Watch6,14, software:10.2&gt;"
        result = name_utils.extract_device_name(device_name)
        expected = "Apple Watch"
        self.assertEqual(result, expected)

    def test_remove_metadata_prefix(self):
        input_value = "HKMetadataKeyExternalUUID"
        result = name_utils.remove_metadata_prefix(input_value)
        expected = "ExternalUUID"
        self.assertEqual(result, expected)
        input_value = "HKDevicePlacementSide"
        result = name_utils.remove_metadata_prefix(input_value)
        expected = "DevicePlacementSide"
        self.assertEqual(result, expected)

    def test_determine_workout_location(self):
        input_value = "0"
        result = name_utils.determine_workout_location(input_value)
        expected = "Outdoor"
        self.assertEqual(result, expected)
        input_value = "1"
        result = name_utils.determine_workout_location(input_value)
        expected = "Indoor"
        self.assertEqual(result, expected)

    def test_remove_record_type_prefix(self):
        input_value = "HKQuantityTypeIdentifierDietaryWater"
        result = name_utils.remove_record_type_prefix(input_value)
        expected = "DietaryWater"
        self.assertEqual(result, expected)
        input_value = "HKCategoryTypeIdentifierSleepAnalysis"
        result = name_utils.remove_record_type_prefix(input_value)
        expected = "SleepAnalysis"
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

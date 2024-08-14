"""
Parses XML Apple health records and converts them into CSV-compatible row structures.

This module provides the `HealthRecordParser` class, which is used to parse
health records stored in XML format and convert them into tuples that can be
exported to CSV files.

Usage example:
    parser = HealthRecordParser(record)
    csv_row = parser.csv_row_structure()
"""

import xml.etree.cElementTree as ET
from config import HeartRateMotionContext
from utils import name_utils as name_utils


class HealthRecordParser:
    def __init__(self, record:  ET.Element):
        """Initializes the HealthRecordParser with an XML record element.

        Args:
            record: An XML Element representing a health record.
        """
        self.record = record
        self.record_type = name_utils.remove_record_type_prefix(
            self.record.get("type"))
        
        self.record_unit = self.record.get("unit")
        self.record_value = self.record.get("value")
        self.record_source_name = self.record.get("sourceName")
        self.record_source_version = self.record.get("sourceVersion")
        self.record_device = self.record.get("device")
        self.record_creation_date = self.record.get("creationDate")
        self.record_start_date = self.record.get("startDate")
        self.record_end_date = self.record.get("endDate")

    def _get_heart_rate_motion_context(self) -> str:
        """Fetches the heart rate motion context from the metadata.

        Iterates through all MetadataEntry elements in the record to find the
        record with the key "HKMetadataKeyHeartRateMotionContext".

        Returns:
            A string representing the heart rate motion context value. If the context
            is not found, "NOT FOUND" is returned.
        """

        metadata_entries = self.record.findall('MetadataEntry')
        for metadata_entry in metadata_entries:
            if metadata_entry.get("key") == "HKMetadataKeyHeartRateMotionContext":
                return HeartRateMotionContext.from_value(int(metadata_entry.get('value')))
        return 'NOT FOUND'

    def _format_heart_rate_record(self) -> tuple:
        """Formats the health record specifically for HeartRate type.

        Returns:
            A tuple containing the formatted heart rate record data, including
            the heart rate motion context.
        """

        return tuple((
            self.record_type,
            self.record_unit,
            self.record_value,
            self.record_source_name,
            self.record_source_version,
            self.record_device,
            self.record_creation_date,
            self.record_start_date,
            self.record_end_date,
            self._get_heart_rate_motion_context()
        ))

    def _get_default_record_data(self) -> tuple:
        """Formats the health record for general data.

        Returns:
            A tuple containing the default formatted record data.
        """
        return tuple((
            self.record_type,
            self.record_unit,
            self.record_value,
            self.record_source_name,
            self.record_source_version,
            self.record_device,
            self.record_creation_date,
            self.record_start_date,
            self.record_end_date,
        ))

    def csv_row_structure(self) -> tuple:
        """Determines the CSV row structure based on the record type.

        Uses record type matching to return the appropriate tuple 
        structure for the record.

        Returns:
            A tuple representing the CSV row structure for the record.
        """
        match self.record_type:
            case 'HeartRate':
                return self._format_heart_rate_record()
            case _:
                return self._get_default_record_data()

import xml.etree.cElementTree as ET

class AppleHealthExportParser:
    def __init__(self):
        pass

    def _generate_root(self) -> ET.Element:
        return NotImplementedError

    def _parse_activity_summary_elements(self) -> None:
        return NotImplementedError
    
    def _parse_workout_elements(self) -> None:
        return NotImplementedError
    
    def _parse_health_record_elements(self) -> None:
        return NotImplementedError
    
    def _parse_gpx_files(self) -> None:
        return NotImplementedError

    def parse_health_elements(self):
        self._parse_gpx_files()
        self._parse_health_record_elements()
        self._parse_activity_summary_elements()
        self._parse_workout_elements()
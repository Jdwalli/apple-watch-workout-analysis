"""
Parses XML Apple health activity summary entries and converts them into CSV-compatible row structures.

This module provides the `ActivitySummaryParser` class, which is used to parse
activity summaries stored in XML format and convert them into tuples that can be
exported to CSV files.

Usage example:
    parser = ActivitySummaryParser(activity_summary)
    csv_row = parser.csv_row_structure()
"""

import xml.etree.cElementTree as ET


class ActivitySummaryParser:
    """Initializes the ActivitySummaryParser with an XML activity_summary element.
    Args:
        record: An XML Element representing a activity summary.
    """

    def __init__(self, activity_summary: ET.Element):
        self.activity_summary = activity_summary

        self._check_tag_validity()

        self.date = self.activity_summary.get("dateComponents")
        self.active_energy_burned = self.activity_summary.get(
            "activeEnergyBurned")
        self.active_energy_burned_goal = self.activity_summary.get(
            'activeEnergyBurnedGoal')
        self.active_energy_burned_unit = self.activity_summary.get(
            'activeEnergyBurnedUnit')
        self.move_time = self.activity_summary.get('appleMoveTime')
        self.move_time_goal = self.activity_summary.get("appleMoveTimeGoal")
        self.exercise_time = self.activity_summary.get('appleExerciseTime')
        self.exercise_time_goal = self.activity_summary.get(
            'appleExerciseTimeGoal')
        self.stand_hours = self.activity_summary.get('appleStandHours')
        self.stand_hours_goal = self.activity_summary.get(
            'appleStandHoursGoal')

    def _check_tag_validity(self):
        """Checks if the tag of the XML element provided to the ActivitySummaryParser is valid.
        Raises:
            TypeError: If the XML element's tag is not "ActivitySummary". The error message includes
                       the actual tag of the provided XML element.
        """
        if self.activity_summary.tag != "ActivitySummary":
            raise TypeError(
                f"The ActivitySummaryParser can only parse ActivitySummary tags. This object's tag is: '{self.activity_summary.tag}'")

    def csv_row_structure(self):
        """Returns the CSV row structure for the activity summary 

        Returns:
            A tuple representing the CSV row structure for the activity summary.
        """
        return tuple((
            self.date,
            self.active_energy_burned,
            self.active_energy_burned_goal,
            self.active_energy_burned_unit,
            self.move_time,
            self.move_time_goal,
            self.exercise_time,
            self.exercise_time_goal,
            self.stand_hours,
            self.stand_hours_goal
        ))

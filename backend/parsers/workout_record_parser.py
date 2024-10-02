"""
Parses Apple health workout data and converts it into CSV-compatible row structures.

This module provides the `WorkoutRouteParser` class, which is used to parse
tracks elements stored in a GPX format and convert them into a dataframe.

This module provides the `WorkoutRecordParser` class, which is used to parse
Workout elements stored in a xml format and convert them into tuples that can
be exported to CSV files.

Usage example:
    workout_tracks = WorkoutRouteParser(tracks)
    df = workout_tracks.to_dataframe()

Usage example:
    workout = WorkoutRecordParser(workout)
    workout_csv_row = workout.csv_row_structure()
"""

import xml.etree.cElementTree as ET
from utils import name_utils as name_utils
from typing import List
import pandas as pd
import config


class WorkoutRouteParser:
    WORKOUT_ROUTE_COLUMNS = [
        "lon",
        "lat",
        "elevation",
        "time",
        "speed",
        "course",
        "hAcc",
        "vAcc",
    ]

    def __init__(self, tracks: List[ET.Element]):
        """Initializes the WorkoutRouteParser with a tracks element.

        Args:
            tracks: A list of ET.Element representing track points.
        """
        self.ns = {"gpx": "http://www.topografix.com/GPX/1/1"}
        self.tracks = tracks
        self.workout_route_data = []

    def _get_track_segments(self, track: ET.Element) -> ET.Element:
        """Retrieves all track segments within a track element.

        Args:
            track: An XML element representing a track from a GPX file.

        Returns:
            A list of XML elements representing the track segments ('trkseg')
            within the provided track element.
        """
        return track.findall('gpx:trkseg', self.ns)

    def _get_track_points(self, track_segment: ET.Element) -> ET.Element:
        """Retrieves all track points within a track element.

        Args:
            track: An XML element representing a track_segment from a GPX file.

        Returns:
            A list of XML elements representing the track points ('trkpt')
            within the provided track element.
        """
        return track_segment.findall('gpx:trkpt', self.ns)

    def _extract_gpx_data(self) -> None:
        """Extracts data from GPX tracks and stores it in the workout_route_data list.

        This method iterates over each track, retrieves its segments, and then extracts
        data from each track point within those segments. The extracted data is converted
        into a CSV-compatible row structure and appended to the workout_route_data list.
        """

        for track in self.tracks:
            for track_segment in self._get_track_segments(track):
                for track_point in self._get_track_points(track_segment):
                    track_point_data = self._to_csv_row_structure(track_point)
                    self.workout_route_data.append(track_point_data)

    def _to_csv_row_structure(self, track_point: ET.Element) -> tuple:
        """Constructs a tuple representing the CSV row structure for a given track point.
        The units of the elements can be found at https://www.topografix.com/GPX/1/1/gpx.xsd

        Args:
            track_point: An XML element representing a track point ('trkpt')
                        from a GPX file.

        Returns:
            A tuple containing the following elements extracted from the track point:
            - Longitude (lon)
            - Latitude (lat)
            - Elevation (ele) (Meters)
            - Time (time)
            - Speed (speed) (Meters Per Second)
            - Course (course) (Decimal Degrees)
            - Horizontal Accuracy (hAcc) (Meters)
            - Vertical Accuracy (vAcc) (Meters)
        """
        elevation = track_point.find('gpx:ele', self.ns).text
        time = track_point.find('gpx:time', self.ns).text
        extension = track_point.find('gpx:extensions', self.ns)
        lon = track_point.get("lon")
        lat = track_point.get("lat")
        speed = extension.find('gpx:speed', self.ns).text
        course = extension.find('gpx:course', self.ns).text
        hAcc = extension.find('gpx:hAcc', self.ns).text
        vAcc = extension.find('gpx:vAcc', self.ns).text

        return (lon, lat, elevation, time, speed, course, hAcc, vAcc)

    def to_dataframe(self) -> pd.DataFrame:
        """Converts the extracted GPX data into a pandas DataFrame.

        This method calls the _extract_gpx_data method to populate the
        workout_route_data list with  data from the GPX tracks.
        It then converts this list into a pandas DataFrame, using the
        WORKOUT_ROUTE_COLUMNS as the column.

        Returns:
            pd.DataFrame: A DataFrame containing the workout route data, with
                          columns for longitude, latitude, elevation, time,
                          speed, course, horizontal accuracy, and vertical accuracy.
        """
        self._extract_gpx_data()
        return pd.DataFrame(self.workout_route_data, columns=self.WORKOUT_ROUTE_COLUMNS)


class WorkoutRecordParser:

    WORKOUT_COLUMNS = [
        "workoutActivityType",
        "duration",
        "durationUnit",
        "sourceName",
        "sourceVersion",
        "device",
        "creationDate",
        "startDate",
        "endDate"
    ]

    WORKOUT_STATISTICS_COLUMNS = [
        "activeEnergyBurned",
        "activeEnergyBurnedUnit",
        "distanceWalkingRunning",
        "distanceWalkingRunningUnit",
        "basalEnergyBurned",
        "basalEnergyBurnedUnit",
        "minimumHeartRate",
        "maximumHeartRate",
        "averageHeartRate",
        "heartRateUnit",
        "stepCount",
        "stepCountUnit",
        "minimumGroundContactTime",
        "maximumGroundContactTime",
        "averageGroundContactTime",
        "groundContactTimeUnit",
        "minimumRunningPower",
        "maximumRunningPower",
        "averageRunningPower",
        "runningPowerUnit",
        "minimumRunningVerticalOscillation",
        "maximumRunningVerticalOscillation",
        "averageRunningVerticalOscillation",
        "runningVerticalOscillationUnit",
        "minimumRunningSpeed",
        "maximumRunningSpeed",
        "averageRunningSpeed",
        "runningSpeedUnit",
        "minimumRunningStrideLength",
        "maximumRunningStrideLength",
        "averageRunningStrideLength",
        "runningStrideLengthUnit",
        "distanceSwimming",
        "distanceSwimmingUnit",
        "distanceCycling",
        "distanceCyclingUnit",
        "swimmingStrokeCount",
        "swimmingStrokeCountUnit"
    ]

    WORKOUT_METADATA_COLUMNS = [
        "indoorWorkout",
        "temperature",
        "humidity",
        "timeZone",
        "averageMETs",
        "physicalEffortEstimationType",
        "elevationAscended",
        "elevationDescended",
        "averageSpeed",
        "maximumSpeed",
        "swimmingLocationType",
        "swimmingStrokeStyle",
        "lapLength",
        "swolfScore",
        "waterSalinity"
    ]

    WORKOUT_ROUTE_COLUMNS = [
        "FileReference"
    ]

    MASTER_WORKOUT_COLUMNS = (
        WORKOUT_COLUMNS +
        WORKOUT_STATISTICS_COLUMNS +
        WORKOUT_METADATA_COLUMNS +
        WORKOUT_ROUTE_COLUMNS
    )

    def __init__(self, workout_record: ET.Element):
        self.workout_record = workout_record
        self.workout_route = self.workout_record.find('WorkoutRoute')
        self.metadata_entries = self.workout_record.findall("MetadataEntry")
        self.workout_statistics = self.workout_record.findall(
            "WorkoutStatistics")
        self.workout_events = self.workout_record.findall('WorkoutEvent')

    def _get_workout_record_data(self) -> tuple:
        """Extracts data recorded for each workout element.

        This method extracts all relevant data collected during the workout
        according to the XML schema:

            <!ATTLIST Workout
            workoutActivityType   CDATA #REQUIRED
            duration              CDATA #IMPLIED
            durationUnit          CDATA #IMPLIED
            totalDistance         CDATA #IMPLIED
            totalDistanceUnit     CDATA #IMPLIED
            totalEnergyBurned     CDATA #IMPLIED
            totalEnergyBurnedUnit CDATA #IMPLIED
            sourceName            CDATA #REQUIRED
            sourceVersion         CDATA #IMPLIED
            device                CDATA #IMPLIED
            creationDate          CDATA #IMPLIED
            startDate             CDATA #REQUIRED
            endDate               CDATA #REQUIRED
            >
        """

        return (
            self.workout_record.get("workoutActivityType"),
            self.workout_record.get("duration"),
            self.workout_record.get("durationUnit"),
            self.workout_record.get("sourceName"),
            self.workout_record.get("sourceVersion"),
            name_utils.extract_device_name(self.workout_record.get("device")),
            self.workout_record.get("creationDate"),
            self.workout_record.get("startDate"),
            self.workout_record.get("endDate"),
        )

    def _get_workout_file_reference(self) -> tuple:
        """Extracts file reference recorded for a workout element if present.

        This method extracts the file reference if it exist on the workout element:

            <!ELEMENT FileReference EMPTY>
            <!ATTLIST FileReference
            path CDATA #REQUIRED
            >
        """
        file_path = ""
        if self.workout_route:
            file_reference = self.workout_route.find('FileReference')
            if file_reference is not None and "path" in file_reference.attrib:
                file_path = file_reference.attrib["path"]
        return (file_path,)

    def _get_workout_metadata(self, metadata_list: List[ET.Element]) -> tuple:
        indoorWorkout = ""
        temperature = ""
        humidity = ""
        timeZone = ""
        averageMETs = ""
        physicalEffortEstimationType = ""
        elevationAscended = ""
        elevationDescended = ""
        averageSpeed = ""
        maximumSpeed = ""
        swimmingLocationType = ""
        swimmingStrokeStyle = ""
        lapLength = ""
        swolfScore = ""
        waterSalinity = ""

        for metadata in metadata_list:
            match metadata.get("key"):
                case "HKIndoorWorkout":
                    indoorWorkout = name_utils.determine_workout_location(
                        metadata.get("value")
                    )
                case "HKWeatherTemperature":
                    temperature = metadata.get("value", "")
                case "HKWeatherHumidity":
                    humidity = metadata.get("value", "")
                case "HKTimeZone":
                    timeZone = metadata.get("value", "")
                case "HKAverageMETs":
                    averageMETs = metadata.get("value", "")
                case "HKPhysicalEffortEstimationType":
                    if value := metadata.get("value"):
                        physicalEffortEstimationType = (
                            config.PhysicalEffortEstimationType.from_value(
                                int(value)
                            )
                        )
                case "HKElevationAscended":
                    elevationAscended = metadata.get("value", "")
                case "HKElevationDescended":
                    elevationDescended = metadata.get("value", "")
                case "HKAverageSpeed":
                    averageSpeed = metadata.get("value", "")
                case "HKMaximumSpeed":
                    maximumSpeed = metadata.get("value", "")
                case "HKSwimmingLocationType":
                    swimmingLocationType = config.SwimmingLocations.from_value(
                        int(metadata.get("value"))
                    )
                case "HKSwimmingStrokeStyle":
                    swimmingStrokeStyle = config.SwimmingStrokeStyles.from_value(
                        int(metadata.get("value"))
                    )
                case "HKLapLength":
                    lapLength = metadata.get("value", "")
                case "HKSWOLFScore":
                    swolfScore = metadata.get("value", "")
                case "HKWaterSalinity":
                    waterSalinity = metadata.get("value", "")
        return (
            indoorWorkout,
            temperature,
            humidity,
            timeZone,
            averageMETs,
            physicalEffortEstimationType,
            elevationAscended,
            elevationDescended,
            averageSpeed,
            maximumSpeed,
            swimmingLocationType,
            swimmingStrokeStyle,
            lapLength,
            swolfScore,
            waterSalinity
        )

    def _get_workout_statistics(self, workout_statistics: List[ET.Element]):
        """Extracts statistics recorded for each workout element.

        This method extracts all relevant data collected during the workout
        according to the XML schema:
            <!ELEMENT WorkoutStatistics EMPTY>
            <!ATTLIST WorkoutStatistics
            type                 CDATA #REQUIRED
            startDate            CDATA #REQUIRED
            endDate              CDATA #REQUIRED
            average              CDATA #IMPLIED
            minimum              CDATA #IMPLIED
            maximum              CDATA #IMPLIED
            sum                  CDATA #IMPLIED
            unit                 CDATA #IMPLIED
            >
        """
        activeEnergyBurned = ""
        activeEnergyBurnedUnit = ""
        distanceWalkingRunning = ""
        distanceWalkingRunningUnit = ""
        basalEnergyBurned = ""
        basalEnergyBurnedUnit = ""
        minimumHeartRate = ""
        maximumHeartRate = ""
        averageHeartRate = ""
        heartRateUnit = ""
        stepCount = ""
        stepCountUnit = ""
        minimumGroundContactTime = ""
        maximumGroundContactTime = ""
        averageGroundContactTime = ""
        groundContactTimeUnit = ""
        minimumRunningPower = ""
        maximumRunningPower = ""
        averageRunningPower = ""
        runningPowerUnit = ""
        minimumRunningVerticalOscillation = ""
        maximumRunningVerticalOscillation = ""
        averageRunningVerticalOscillation = ""
        runningVerticalOscillationUnit = ""
        minimumRunningSpeed = ""
        maximumRunningSpeed = ""
        averageRunningSpeed = ""
        runningSpeedUnit = ""
        minimumRunningStrideLength = ""
        maximumRunningStrideLength = ""
        averageRunningStrideLength = ""
        runningStrideLengthUnit = ""
        distanceSwimming = ""
        distanceSwimmingUnit = ""
        distanceCycling = ""
        distanceCyclingUnit = ""
        swimmingStrokeCount = ""
        swimmingStrokeCountUnit = ""

        for statistic in workout_statistics:
            match statistic.get("type"):
                case "HKQuantityTypeIdentifierActiveEnergyBurned":
                    activeEnergyBurned = float(statistic.get("sum"))
                    activeEnergyBurnedUnit = statistic.get("unit")

                case "HKQuantityTypeIdentifierDistanceWalkingRunning":
                    distanceWalkingRunning = float(statistic.get("sum"))
                    distanceWalkingRunningUnit = statistic.get("unit")

                case "HKQuantityTypeIdentifierBasalEnergyBurned":
                    basalEnergyBurned = float(statistic.get("sum"))
                    basalEnergyBurnedUnit = statistic.get("unit")

                case "HKQuantityTypeIdentifierHeartRate":
                    averageHeartRate = float(statistic.get("average"))
                    minimumHeartRate = float(statistic.get("minimum"))
                    maximumHeartRate = float(statistic.get("maximum"))
                    heartRateUnit = statistic.get("unit")

                case "HKQuantityTypeIdentifierStepCount":
                    stepCount = float(statistic.get("sum"))
                    stepCountUnit = statistic.get("unit")

                case "HKQuantityTypeIdentifierGroundContactTime":
                    minimumGroundContactTime = float(statistic.get("minimum"))
                    maximumGroundContactTime = float(statistic.get("maximum"))
                    averageGroundContactTime = float(statistic.get("average"))
                    groundContactTimeUnit = statistic.get("unit")

                case "HKQuantityTypeIdentifierRunningPower":
                    minimumRunningPower = float(statistic.get("minimum"))
                    maximumRunningPower = float(statistic.get("maximum"))
                    averageRunningPower = float(statistic.get("average"))
                    runningPowerUnit = statistic.get("unit")

                case "HKQuantityTypeIdentifierRunningVerticalOscillation":
                    minimumRunningVerticalOscillation = float(
                        statistic.get("minimum"))
                    maximumRunningVerticalOscillation = float(
                        statistic.get("maximum"))
                    averageRunningVerticalOscillation = float(
                        statistic.get("average"))
                    runningVerticalOscillationUnit = statistic.get("unit")

                case "HKQuantityTypeIdentifierRunningSpeed":
                    minimumRunningSpeed = float(statistic.get("minimum"))
                    maximumRunningSpeed = float(statistic.get("maximum"))
                    averageRunningSpeed = float(statistic.get("average"))
                    runningSpeedUnit = statistic.get("unit")

                case "HKQuantityTypeIdentifierRunningStrideLength":
                    minimumRunningStrideLength = float(
                        statistic.get("minimum"))
                    maximumRunningStrideLength = float(
                        statistic.get("maximum"))
                    averageRunningStrideLength = float(
                        statistic.get("average"))
                    runningStrideLengthUnit = statistic.get("unit")

                case "HKQuantityTypeIdentifierDistanceSwimming":
                    distanceSwimming = float(statistic.get("sum"))
                    distanceSwimmingUnit = statistic.get("unit")

                case "HKQuantityTypeIdentifierDistanceCycling":
                    distanceCycling = float(statistic.get("sum"))
                    distanceCyclingUnit = statistic.get("unit")

                case "HKQuantityTypeIdentifierSwimmingStrokeCount":
                    swimmingStrokeCount = float(statistic.get("sum"))
                    swimmingStrokeCountUnit = statistic.get("unit")

        return (
            activeEnergyBurned,
            activeEnergyBurnedUnit,
            distanceWalkingRunning,
            distanceWalkingRunningUnit,
            basalEnergyBurned,
            basalEnergyBurnedUnit,
            minimumHeartRate,
            maximumHeartRate,
            averageHeartRate,
            heartRateUnit,
            stepCount,
            stepCountUnit,
            minimumGroundContactTime,
            maximumGroundContactTime,
            averageGroundContactTime,
            groundContactTimeUnit,
            minimumRunningPower,
            maximumRunningPower,
            averageRunningPower,
            runningPowerUnit,
            minimumRunningVerticalOscillation,
            maximumRunningVerticalOscillation,
            averageRunningVerticalOscillation,
            runningVerticalOscillationUnit,
            minimumRunningSpeed,
            maximumRunningSpeed,
            averageRunningSpeed,
            runningSpeedUnit,
            minimumRunningStrideLength,
            maximumRunningStrideLength,
            averageRunningStrideLength,
            runningStrideLengthUnit,
            distanceSwimming,
            distanceSwimmingUnit,
            distanceCycling,
            distanceCyclingUnit,
            swimmingStrokeCount,
            swimmingStrokeCountUnit
        )

    def csv_row_structure(self) -> tuple:
        """Returns the combined CSV row structure for the workout. 

        Returns:
            A tuple representing the CSV row structure for the workout.
        """
        return self._get_workout_record_data() + self._get_workout_statistics(self.workout_statistics) + self._get_workout_metadata(self.metadata_entries) + self._get_workout_file_reference()

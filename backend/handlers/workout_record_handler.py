import pandas as pd
import numpy as np
from utils import file_utils as file_utils
import config
import os
from typing import List

def load_workout_records_into_dataframe() -> pd.DataFrame:
    workout_csv_path = os.path.join(config.WORKOUT_ELEMENTS_DIRECTORY,
                                    config.WORKOUTS_SUMMARY_FILE_NAME)
    if file_utils.file_exists(workout_csv_path):
        return pd.read_csv(workout_csv_path)
    return pd.DataFrame()


def load_workout_records_from_date(dataframe: pd.DataFrame, workout_start_date: str) -> List:
    """
    Retrieve workout data based on workout type and start date.

    Args:
        dataframe (pd.DataFrame): DataFrame containing workout data.
        workout_start_date (str): Start date of the workout.

    Returns:
        dict or None: A dictionary containing the first matching workout data row
                      if a matching workout is found, otherwise returns None.
    """
    if not dataframe.empty:
        dataframe = dataframe.replace(np.nan, "", regex=True)

    dataframe["date"] = pd.to_datetime(dataframe["startDate"]).dt.date
    workout_start_date = pd.to_datetime(workout_start_date)

    match: pd.DataFrame = dataframe[
        (dataframe["date"] == pd.to_datetime(workout_start_date).date())
    ]
    del match['date']

    return None if match.empty else match.to_dict(orient='records')


def load_unique_workout_dates(dataframe: pd.DataFrame) -> List:
    if not dataframe.empty:
        dataframe = dataframe.replace(np.nan, "", regex=True)

    dataframe["date"] = pd.to_datetime(dataframe["startDate"]).dt.strftime('%Y-%m-%d')

    return dataframe["date"].unique().tolist()


def load_workout_record_gpx_data(workout_file_reference: str):
    gpx_file_path = file_utils.format_workout_reference_into_path(
        workout_file_reference)

    #TODO Add better method to ensure file is not a directory
    if file_utils.file_exists(gpx_file_path) and not os.path.isdir(gpx_file_path):
        df = pd.read_csv(gpx_file_path)
        return {
            'longitude': df['lon'].to_list(),
            'latitude': df['lat'].to_list(),
            'elevation': df['elevation'].to_list(),
            'time': df['time'].to_list(),
            'speed': df['speed'].to_list(),
            'course': df['course'].to_list(),
            'hAcc': df['hAcc'].to_list(),
            'vAcc': df['vAcc'].to_list()
        }
    return {}

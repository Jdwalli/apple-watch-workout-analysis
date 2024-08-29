import pandas as pd
import numpy as np
from utils import file_utils as file_utils
import config
import os
from typing import List

from record_handler import load_record


def load_workout_csv():
    workout_csv_path = os.path.join(config.WORKOUT_ELEMENTS_DIRECTORY,
                                    config.WORKOUTS_SUMMARY_FILE_NAME)
    if file_utils.file_exists(workout_csv_path):
        return pd.read_csv(workout_csv_path)
    return None


def get_workouts_from_date(dataframe: pd.DataFrame, workout_start_date: str) -> List:
    """
    Retrieve workout data based on workout type and start date.

    Args:
        dataframe (pd.DataFrame): DataFrame containing workout data.
        workout_type (str): Type of the workout.
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
        (dataframe["date"] == pd.to_datetime(workout_start_date))
    ]
    del match['date']

    return None if match.empty else match.to_dict(orient='records')

def get_workout_gpx_data(workout_gpx_path: str):
    df = load_record()
    # replace gpx with csv /workout-routes/route_2024-03-28_12.54am.gpx


    {
                        'longitude': [],
                        'latitude': [],
                        'elevation': [],
                        'time': [],
                        'speed': [],
                        'course': [],
                        'hAcc': [],
                        'vAcc': []
                    }
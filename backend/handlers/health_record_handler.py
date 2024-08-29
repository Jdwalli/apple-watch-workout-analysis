import pandas as pd
import os

from utils import file_utils as file_utils

def load_heart_rate_health_record_into_dataframe(record_path) -> pd.DataFrame:
    if file_utils.file_exists(record_path):
        return pd.read_csv(record_path)
    return pd.DataFrame()

def load_health_record_into_dataframe(record_name: str) -> pd.DataFrame:
    record_path = os.path.join(
        file_utils.match_record_type_to_directory(record_name), f'{record_name}.csv')
    
    if record_name == "HeartRate":
        return load_heart_rate_health_record_into_dataframe(record_path)

    return pd.read_csv(record_path) if file_utils.file_exists(record_path) else pd.DataFrame()


def load_record_between_timestamps(record_name: str, start_time: str, end_time: str) -> pd.DataFrame:
    df = load_health_record_into_dataframe(record_name)

    if not df.empty:
        df["startDate"] = pd.to_datetime(df["startDate"])
        df["endDate"] = pd.to_datetime(df["endDate"])

        return df[
            (df["startDate"] >= start_time) &
            (df["endDate"] <= end_time)
        ]

    return pd.DataFrame()


def load_health_record_into_chart_format(record_name: str, start_date: str, end_date: str) -> dict[str, list]:
    df = load_record_between_timestamps(record_name, start_date, end_date)

    if df.empty:
        return {}
    
    df['startDate'] = df['startDate'].apply(
        lambda x: x.strftime('%Y-%m-%d %H:%M:%S %z'))
    
    return {
        "time": df['startDate'].to_list(),
        "value": df['value'].to_list()
    }

import pandas as pd
import numpy as np
import os


from utils import file_utils as file_utils


def load_record(record_name: str) -> pd.DataFrame:
    record_path = os.path.join(
        file_utils.match_record_type_to_directory(record_name), f'{record_name}.csv')

    return pd.read_csv(record_path) if file_utils.file_exists(record_path) else pd.DataFrame()


def load_record_between_dates(record_name: str, start_date: str, end_date: str) -> pd.DataFrame:
    df = load_record(record_name)
    if not df.empty:
        df["startDate"] = pd.to_datetime(df["startDate"])
        df["endDate"] = pd.to_datetime(df["endDate"])
        return df[
            (df["startDate"] >= start_date) &
            (df["endDate"] <= end_date)
        ]
    return pd.DataFrame()


def load_record_into_chart_data(record_name: str, start_date: str, end_date: str) -> dict[str, list]:
    df = load_record_between_dates(record_name, start_date, end_date)
    if df.empty:
        return {}
    df['startDate'] = df['startDate'].apply(
        lambda x: x.strftime('%Y-%m-%d %H:%M:%S %z'))
    return {
        "time": df['startDate'].to_list(),
        "value": df['value'].to_list()
    }

import requests
import pandas as pd
from matplotlib import pyplot as plt

def get_data(api_key, series_id):
    url = 'https://api.stlouisfed.org/fred/series/observations?series_id=' + series_id + '&api_key=' + api_key + '&file_type=json'
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data['observations'])
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index('date')
    df = df.drop(columns = ['realtime_start', 'realtime_end'])
    df = df.rename(columns = {'value': series_id})
    return df


def get_data_multiple(api_key, series_id_list):
    df = get_data(api_key, series_id_list[0])
    for series_id in series_id_list[1:]:
        df = df.join(get_data(api_key, series_id))
    return df

import pandas as pd
import glob
import numpy as np
stations = pd.read_csv('TH_weather/TH_stations.tsv', sep='\t')
stations
files = glob.glob('TH_weather/*.tsv')
files = files[1:]
files.sort()
files = files[-2:]
dfs = []
for file in files:
    dfs.append(pd.read_csv(file, sep='\t'))
    weather_dfs = pd.concat(dfs)
    weather_dfs['PRCP_letter'] = weather_dfs['PRCP'].apply(lambda x: x[-1])
    weather_dfs['PRCP_numeric'] = weather_dfs['PRCP'].apply(lambda x: float(x[:-1]))
    weather_dfs['PRCP_letter'].unique()
    weather_dfs['PRCP_letter'].value_counts()
    weather_dfs['PRCP_numeric'] = weather_dfs['PRCP_numeric'].apply(lambda x: 0 if x >= 99.9 else x)
    weather_dfs['PRCP_numeric_mm'] = weather_dfs['PRCP_numeric'] * 100 * 25.4
    weather_dfs['PRCP_numeric_mm'].max()
    weather_dfs[weather_dfs['PRCP_numeric_mm'] == weather_dfs['PRCP_numeric_mm'].max()]
    weather_dfs['PRCP_numeric_mm'].apply(lambda x: np.round(x, 2)).hist()
    weather_dfs['YEARMODA'] = pd.to_datetime(weather_dfs['YEARMODA'], format='%Y%m%d')
    weather_dfs['TEMP_celsius'] = weather_dfs['TEMP'].apply(lambda x: (x - 32) * (5 / 9))
    weather_dfs[['YEARMODA', 'TEMP_celsius', 'PRCP_numeric_mm']].head()
    weather_subset = weather_dfs.groupby(pd.Grouper(key='YEARMODA', freq='M'))[
        'TEMP_celsius', 'PRCP_numeric_mm'].median().reset_index()
    weather_subset['YEARMODA'] = weather_subset['YEARMODA'].apply(
        lambda x: pd.datetime(year=x.year, month=x.month, day=1))
    weather_subset.head()
    weather_subset.to_csv('./power_demand/weather/TH_weather_21_22.csv', index=False)
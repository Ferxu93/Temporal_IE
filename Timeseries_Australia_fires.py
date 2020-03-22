from time import strptime

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_colwidth', 100)
pd.set_option('display.max_columns', 30)
pd.set_option('display.max_rows', 30)
pd.options.display.float_format = '{:.3f}'.format



Timeseries_Austalia_fires_df = pd.read_csv('/Users/fer/Downloads/fires-from-space-australia-and-new-zeland/'
                                           'fire_nrt_V1_96617.csv')
print(Timeseries_Austalia_fires_df)
print(type(Timeseries_Austalia_fires_df))
print(Timeseries_Austalia_fires_df.describe())
print(Timeseries_Austalia_fires_df.dtypes)

Timeseries_Austalia_fires_df.acq_date = pd.to_datetime(Timeseries_Austalia_fires_df.acq_date, format='%Y-%m-%d')
print(Timeseries_Austalia_fires_df)
print(Timeseries_Austalia_fires_df.dtypes)
Timeseries_Austalia_fires_df.acq_time = pd.to_datetime(Timeseries_Austalia_fires_df.acq_time, format='%H%M')

print(Timeseries_Austalia_fires_df)
print(Timeseries_Austalia_fires_df.dtypes)

# LET´S TRANSFORM TO TIMESERIES

Timeseries_Austalia_fires_df.index = Timeseries_Austalia_fires_df.acq_date
print(Timeseries_Austalia_fires_df)

Fires_df = Timeseries_Austalia_fires_df.groupby(by='daynight')['daynight'].count().to_frame()
print(Fires_df) #number of fires during the day and the night

daynight_df = Timeseries_Austalia_fires_df.groupby(by=['daynight', 'track'])['frp'].max().to_frame()
print(daynight_df)

months_df = Timeseries_Austalia_fires_df.scan.resample('M').mean().to_frame()
print(months_df)

from time import strptime

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_colwidth', 100)
pd.set_option('display.max_columns', 30)
pd.set_option('display.max_rows', 30)
pd.options.display.float_format = '{:.3f}'.format

Bitcoin_TimeSeries_df = pd.read_csv('/Users/fer/Desktop/BlockChain_Train_csv.csv')
print(Bitcoin_TimeSeries_df)
print(type(Bitcoin_TimeSeries_df))
print(Bitcoin_TimeSeries_df.dtypes)

dates_reformated = []
for date in Bitcoin_TimeSeries_df.Date:
   new_date = str(date).rsplit('-')[0]+'-'+str(date).rsplit('-')[1]+'-'+'20'+str(date).rsplit('-')[2]
   dates_reformated.append(new_date)

Bitcoin_TimeSeries_df.Date = dates_reformated
Bitcoin_TimeSeries_df.Date = pd.to_datetime(Bitcoin_TimeSeries_df.Date)

print(Bitcoin_TimeSeries_df)
print(Bitcoin_TimeSeries_df.dtypes)

# RESAMPLE = GROUP BY

Bitcoin_TimeSeries_df.index = Bitcoin_TimeSeries_df.Date
Anual_Bitcoins_in_circulation = Bitcoin_TimeSeries_df.Bitcoins_in_circulation.resample('A').max()
print(Anual_Bitcoins_in_circulation)
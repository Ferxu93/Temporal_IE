import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_colwidth', 100)
pd.set_option('display.max_columns', 30)
pd.set_option('display.max_rows', 300)
pd.options.display.float_format = '{:.3f}'.format

Blockchain_df = pd.read_csv('/Users/fer/Desktop/BlockChain_Train_csv.csv', sep=',')
Blockchain_df['Date'] = pd.to_datetime(Blockchain_df.Date)
print(Blockchain_df)

Blockchain_subdf = Blockchain_df.iloc[:, 0:4]
print(Blockchain_subdf)

print(Blockchain_df.dtypes)
print('\nThis are the stadistics from the Bitcoins in circulation: \n',
      Blockchain_df.Bitcoins_in_circulation.describe())

Blockchain_subdf = Blockchain_df.USD_Exchange_Trade_Volume.mean()
print(' This is the mean from the exchange: ', Blockchain_subdf)

Blockchain_subdf = Blockchain_df['USD/EUR'].max(), Blockchain_df['USD/EUR'].min()
print('This is the max: ', Blockchain_df['USD/EUR'].max(), '\nThis is the min: ', Blockchain_df['USD/EUR'].min())

Blockchain_df.index = Blockchain_df.Date
Blockchain_df = Blockchain_df.iloc[:, 1:66]
print(Blockchain_df)

'''MANIPULATION OF TIME SERIES'''

Blockchain_USDEUR_df = Blockchain_df['USD/EUR']
print(Blockchain_USDEUR_df)
print(type(Blockchain_USDEUR_df))

Blockchain_USDEUR_plot = 0
if Blockchain_USDEUR_plot == 1:
     # Blockchain_USDEUR_df.plot(kind='line', color='red')
     # Blockchain_USDEUR_df.plot(kind='hist', color='blue', bins=10)
      Blockchain_USDEUR_df.plot(kind='hist', color='lightgreen', bins=10, cumulative=True)
     # Blockchain_USDEUR_df.plot(kind='hist', color='lightblue', bins=len(Blockchain_USDEUR_df), density=True, range=(0,11))
      plt.grid(), plt.show(), plt.clf()

'''PRINTING IQR'''
q = [0.25, 0.75]
IQR = Blockchain_USDEUR_df.quantile(q)
print(IQR)
print(Blockchain_USDEUR_df.describe())

'''PLOTING IQR'''
Blockchain_USDEUR_boxplot = 0
if Blockchain_USDEUR_boxplot == 1:
      Blockchain_USDEUR_df.plot(kind='box', color='blue')
      plt.grid(), plt.show(), plt.clf()

'''MULTIPLOTING IN ONE PLOT'''
Multiploting = 0
if Multiploting == 1:
      Blockchain_df['USD/EUR'].plot(kind='line', color='red')
      Blockchain_df['USD/JPY'].plot(kind='line', color='green')
      Blockchain_df['USD/CHF'].plot(kind='line', color='purple')
      plt.grid(), plt.show(), plt.clf()

Correlation = Blockchain_df['USD/EUR'].corr(Blockchain_df['USD/CHF'])
print(Correlation)


'''MULTIPLOTING IN SUBPLOTS'''

Subploting1 = 0
if Subploting1 == 1:
    fig, axs = plt.subplots(nrows=3, ncols=1)
    Blockchain_df['USD/EUR'].plot(kind='line', color='red', ax=axs[0])
    Blockchain_df['USD/JPY'].plot(kind='line', color='green', ax=axs[1])
    Blockchain_df['USD/CHF'].plot(kind='line', color='purple', ax=axs[2])
    plt.grid(), plt.show(), plt.clf()


'''GROUPING BY (GENERAL METHOD & TIME METHOD)'''
# for each difficulty level, get the mean of Bitcoins in circulation:
Blockchain_mean_difficulty = Blockchain_df.groupby(by=['Difficulty'])['Bitcoins_in_circulation'].mean()
print(Blockchain_mean_difficulty)

Blockchain_mean_difficulty_plot = 0
if Blockchain_mean_difficulty_plot ==1:
    Blockchain_mean_difficulty.plot(kind='line', color= 'blue')
    plt.grid(), plt.show(), plt.clf()

'''TIME METHOD'''
# Max value of the relation USD/JPY for each month:
Blockchain_USDJPY_maxvalue = Blockchain_df['USD/JPY'].resample('M').max()
print(Blockchain_USDJPY_maxvalue)

Blockchain_USDJPY_maxvalue_plot = 0
if Blockchain_USDJPY_maxvalue_plot == 1:
    Blockchain_USDJPY_maxvalue.plot(kind='line', color='red')
    plt.grid(), plt.show(), plt.clf()

'''SUBSETTING TS-BASED DATAFRAMES (+ NANS MANAGEMENT)'''

Nov1111 = Blockchain_df.loc['2011-11-11', 'Bitcoins_in_circulation']
print('\nThe Bitcoins in circulation for this day are:', Nov1111)

# To select on a desired date range:
My_date_range = Blockchain_df.loc['2012-10-18':'2018-05-31']
print('During this two dates the Bitcoins in circulation were: ', My_date_range)


#Blockchain_df = Blockchain_df.dropna()
#Blockchain_df = Blockchain_df.fillna(0)
#Blockchain_df['USD/EUR'] = Blockchain_df['USD/EUR'].fillna(method='bfill')
#Blockchain_df['USD/EUR'] = Blockchain_df['USD/EUR'].interpolate(how='quadratic')
#print(Blockchain_df)


'''SMOOTHING SERIES'''

usdjpy = Blockchain_df['USD/JPY']
usdjpy_rolled = Blockchain_df['USD/JPY'].rolling(window=8).mean()
rolled_Vs_nonrolled_plot = 0
if rolled_Vs_nonrolled_plot == 1:
    usdjpy.plot(kind='line', color='red')
    usdjpy_rolled.plot(kind='line', color='darkblue')
    plt.grid(), plt.show(), plt.clf()

'''ROLLED AND NONROLLED DF & COLUMN RENAMING'''

usdjpy_df = pd.DataFrame(usdjpy, usdjpy_rolled).rename(columns={'USD/JPY': 'ROLLED'})
usdjpy_df['NONROLLED'] = Blockchain_df['USD/JPY'].values
usdjpy_df['ROLLED'] = usdjpy_df.index
usdjpy_df.index = Blockchain_df.index
print(usdjpy_df.head(40))

year_df = pd.DatetimeIndex

'''LAMBDAS(a one-liner great option)'''

usdeur_add1 = Blockchain_df['USD/EUR'].apply(lambda x: x+1)
print('\nthis is :\n', usdeur_add1)

'''CORRELATION ANALYSIS: BASE DATA VS PERCENTAGE DATA'''

fig, axs = plt.subplots(nrows=2, ncols=1)
Blockchain_df[['Close']].plot(ax=axs[0])
plt.plot(Blockchain_df[['Close']].pct_change())
plt.show()

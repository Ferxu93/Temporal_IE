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

Blockchain_df_close_plot = 0
if Blockchain_df_close_plot == 1:
    fig, axs = plt.subplots(nrows=2, ncols=1)
    Blockchain_df[['Close']].plot(ax=axs[0])
    plt.plot(Blockchain_df[['Close']].pct_change())
    plt.show()

''''CORRELATION AND AUTOCORRELATION (ACF & PLOTTING)'''

Correlation = Blockchain_df['USD/EUR'].corr(Blockchain_df['USD/CHF'])
print('\n This is the correlation between both:', Correlation)


# Imported libraries for Autocorrelation:

from statsmodels.tsa.stattools import acf
from statsmodels.graphics.tsaplots import plot_acf

Autocorrelation = Blockchain_df['Breakeven Inflation Rate'].autocorr()
print('\n This is the Autocorrelation:', Autocorrelation)

Acf = acf(Blockchain_df['Breakeven Inflation Rate'])
print('\n This is the ACF: ', Acf)
print('\n This is the lenght:',len(Acf))

Blockchain_df_acf_plot = 0
if Blockchain_df_acf_plot == 1:
    plot_acf(Blockchain_df['Breakeven Inflation Rate'], lags=20, alpha=0.5)
    plt.show()

'''WHITE NOISE & GAUSSIAN WHITE NOISE'''

Blockchain_df_WN = 0
if Blockchain_df_WN == 1:
    fig, axs = plt.subplots(nrows=3, ncols=1)
    Blockchain_df[['Breakeven Inflation Rate']].plot(ax=axs[0])
    Blockchain_df[['Breakeven Inflation Rate']].plot(kind='hist',alpha=0.8, ax=axs[1])
    plot_acf(Blockchain_df['Breakeven Inflation Rate'],lags=20, alpha=0.2, ax=axs[2])
    plt.show()

'''REGRESSION ANALYSIS'''

import statsmodels.api as sma

Blockchain_df = sma.add_constant(Blockchain_df)
intercept_y = sma.OLS(Blockchain_df['Breakeven Inflation Rate'], Blockchain_df[['const','US Federal funds rate']]).fit()
print('Results:', intercept_y.summary())
print('Constant Coefficient:',intercept_y.params[0])
print('Independent Variable:',intercept_y.params[1])

''' DICKEY FULLER TEST & AUGMENTED DICKEY FULLER TEST'''

from statsmodels.tsa.stattools import adfuller

adfuller_test = adfuller(Blockchain_df['Breakeven Inflation Rate'])
print(adfuller_test)
print('p-value: ', adfuller_test[1])
alpha = 0.05
if adfuller_test[1] > alpha:
    print('The Null Hypothesis cant be rejected: It may not be a Random Walk(IT MAY BE PREDICTABLE)')
else:
    print('The Null Hypothesis is rejected(It is a Random Walk)')


''' WHITE NOISE + RANDOM WALK + RANDOM WALK (WITH DRIFT)'''

White_Noise = np.random.normal(loc=0, scale=1, size=5000)
print('This is my WN:', White_Noise)

White_Noise_plot = 1
if White_Noise_plot == 1:
    fig, axs = plt.subplots(nrows=3, ncols=1)
    pd.DataFrame(White_Noise, columns=['Rnumbers']).plot(ax=axs[0])
    pd.DataFrame(White_Noise, columns=['hist']).plot(kind='hist',alpha=0.8, ax=axs[1])
    plot_acf(White_Noise, lags=20, alpha=0.2, ax=axs[2])
    plt.show()


steps = np.random.normal(loc=0, scale=1, size=500)
steps[0] = 0
Walk = 100 + np.cumsum(steps)
print('This is my Random Walk:', Walk)


steps_plot = 1
if steps_plot == 1:
    # fig, axs = plt.subplots(nrows=3, ncols=1)
    plt.plot(Walk)
    plot_acf(steps, lags=20, alpha=0.2)
    plt.show()

Steps1 = np.random.normal(loc=0.001, scale=0.01, size=500) + 1
Steps1[0] = 1
Walk = 100 * np.cumprod(Steps1)
print('This is my drifted Random Walk: ', Walk)

Steps1_plot = 1
if Steps1_plot == 1:
    # fig, axs = plt.subplots(nrows=3, ncols=1)
    # pd.DataFrame(Steps1, columns=['Steps1nmbers']).plot(ax=axs[0])
    # pd.DataFrame(Steps1, columns=['Step1_hist']).plot(kind='hist', alpha=0.8, ax=axs[1])
    plt.plot(Walk)
    plot_acf(Walk, lags=20, alpha=0.2)
    plt.show()


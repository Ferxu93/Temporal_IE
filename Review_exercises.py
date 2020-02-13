import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import datetime

desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_colwidth', 100)
pd.set_option('display.max_columns', 30)
pd.set_option('display.max_rows', 30)
pd.options.display.float_format = '{:.3f}'.format

Blockchain_df = pd.read_csv('/Users/fer/Desktop/BlockChain_Train_csv.csv', sep=',')
print(Blockchain_df)

Blockchain_df.index = Blockchain_df.Date
Blockchain_loc = Blockchain_df.iloc[:, [5, 11]]
print(Blockchain_loc)

print('ATRIBUTES: \n')

print('Those are the types inside of the columns: \n\n ', Blockchain_loc.dtypes)
print('\nThis is the info inside of the columns which tells me if there are any nulls: \n\n: ', Blockchain_loc.info())
print(' \nThis describes the statistics inside of the assigned columns: \n\n', Blockchain_loc.describe())
print('  \n Those are the dimensions of the columns: \n\n ', Blockchain_loc.shape)

Blockchain_BlockSize = Blockchain_loc['BlockSize']

Blockchain_BlockSize_plot = 0
if Blockchain_BlockSize_plot == 1:
    Blockchain_BlockSize.plot(kind= 'box')
    plt.grid(), plt.show(), plt.clf()

q = [0.40, 0.80]
IQR = Blockchain_BlockSize.quantile(q)
print(IQR)
print(Blockchain_BlockSize.describe())

IQR_plot = 0
if IQR_plot== 1:
    IQR.plot(kind='box')
    plt.title('IQR_BOXPLOT')
    plt.grid(), plt.show(), plt.clf()

Blockchain_Difficulty = Blockchain_loc['Difficulty']

Blockchain_Difficulty_plot = 0
if Blockchain_Difficulty_plot == 1:
    Blockchain_Difficulty.plot()
    plt.grid(), plt.show(), plt.clf()

'''TRANSFORM AND SEPARATE A DATE IN DIFFERENT COLUMNS '''

Blockchain_df['Year'] = pd.to_datetime(Blockchain_df.Date, format='%d-%m-%Y', infer_datetime_format=True).dt.year
Blockchain_df['Month'] = pd.to_datetime(Blockchain_df.Date, format='%d-%m-%Y', infer_datetime_format=True).dt.month
Blockchain_df['Day'] = pd.to_datetime(Blockchain_df.Date, format='%d-%m-%Y', infer_datetime_format=True).dt.day
Blockchain_df['Year_as_String'] = Blockchain_df.Date.str[-2:]
print(Blockchain_df)

'''BASE DATA Vs PERCENTAGE DATA'''

Blockchain_df_GTI = Blockchain_df['Google Trends Interest']
print(Blockchain_df_GTI)

Blockchain_df_GTI_plot = 1
if Blockchain_df_GTI_plot == 1:
    fig, axs = plt.subplots(nrows=2, ncols=1)
    Blockchain_df[['Google Trends Interest']].plot(ax=axs[0])
    plt.plot(Blockchain_df[['Google Trends Interest']].pct_change())
    plt.show()


'''WHITE NOISE + DICKEY FULLER TEST + RANDOM WALK + ACF : '''

'''WHITE NOISE & GAUSSIAN WHITE NOISE'''

Blockchain_df_WN = 0
if Blockchain_df_WN == 1:
    fig, axs = plt.subplots(nrows=3, ncols=1)
    Blockchain_df[['Google Trends Interest']].plot(ax=axs[0])
    Blockchain_df[['Google Trends Interest']].plot(kind='hist',alpha=0.8, ax=axs[1])
    plot_acf(Blockchain_df[' '],lags=20, alpha=0.2, ax=axs[2])
    plt.show()

'''REGRESSION ANALYSIS'''

import statsmodels.api as sma

Blockchain_df = sma.add_constant(Blockchain_df)
intercept_y = sma.OLS(Blockchain_df['Google Trends Interest'], Blockchain_df[['const','GTrends Normalized']]).fit()
print('Results:', intercept_y.summary())
print('Constant Coefficient:',intercept_y.params[0])
print('Independent Variable:',intercept_y.params[1])

''' DICKEY FULLER TEST & AUGMENTED DICKEY FULLER TEST'''

from statsmodels.tsa.stattools import adfuller

adfuller_test = adfuller(Blockchain_df['Google Trends Interest'])
print(adfuller_test)
print('p-value: ', adfuller_test[1])
alpha = 0.05
if adfuller_test[1] > alpha:
    print('The Null Hypothesis cant be rejected: It may not be a Random Walk(IT MAY BE PREDICTABLE)')
else:
    print('The Null Hypothesis is rejected(It is a Random Walk)')


'''ACF'''

from statsmodels.tsa.stattools import acf
from statsmodels.graphics.tsaplots import plot_acf

Autocorrelation = Blockchain_df['Google Trends Interest'].autocorr()
print('\n This is the Autocorrelation:', Autocorrelation)

Acf = acf(Blockchain_df['Google Trends Interest'])
print('\n This is the ACF: ', Acf)
print('\n This is the lenght:',len(Acf))

Blockchain_df_acf_plot = 1
if Blockchain_df_acf_plot == 1:
    plot_acf(Blockchain_df['Google Trends Interest'], lags=20, alpha=0.5)
    plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_colwidth', 100)
pd.set_option('display.max_columns', 30)
pd.set_option('display.max_rows', 300)
pd.options.display.float_format = '{:.3f}'.format



coronavirus_df = pd.read_csv('/Users/fer/Desktop/Coronavirus.csv', sep=';')
print(coronavirus_df)

Corona_deaths = coronavirus_df['Confirmed']
Corona_deaths_rolled = coronavirus_df['Deaths'].rolling(window=8).mean()
rolled_Vs_nonrolled_plot = 1
if rolled_Vs_nonrolled_plot == 1:
   Corona_deaths.plot(kind='line', color='red')
   Corona_deaths.plot(kind='line', color='darkblue')
   plt.grid(), plt.show(), plt.clf()

coronavirus_df_close_plot = 1
if coronavirus_df_close_plot == 1:
    fig, axs = plt.subplots(nrows=2, ncols=1)
    coronavirus_df[['Deaths']].plot(ax=axs[0])
    plt.plot(coronavirus_df[['Deaths']].pct_change())
    plt.show()

from statsmodels.tsa.stattools import acf
from statsmodels.graphics.tsaplots import plot_acf

Autocorrelation = coronavirus_df['Deaths'].autocorr()
print('\n This is the Autocorrelation:', Autocorrelation)

Acf = acf(coronavirus_df['Deaths'])
print('\n This is the ACF: ', Acf)
print('\n This is the lenght:',len(Acf))

Correlation = coronavirus_df['Confirmed'].corr(coronavirus_df['Deaths'])
print('\n This is the correlation between both:', Correlation)

Corona_deaths_boxplot = 1
if Corona_deaths_boxplot == 1:
      coronavirus_df.plot(kind='box', color='blue')
      plt.grid(), plt.show(), plt.clf()

Multiploting = 1
if Multiploting == 1:
      coronavirus_df['Deaths'].plot(kind='line', color='red')
      coronavirus_df['Confirmed'].plot(kind='line', color='green')
      coronavirus_df['Recovered'].plot(kind='line', color='purple')
      plt.grid(), plt.show(), plt.clf()

'''WHITE NOISE & GAUSSIAN WHITE NOISE'''

coronavirus_df_WN = 1
if coronavirus_df_WN == 1:
    fig, axs = plt.subplots(nrows=2, ncols=1)
    coronavirus_df[['Deaths']].plot(ax=axs[0])
    coronavirus_df[['Deaths']].plot(kind='hist',alpha=0.8, ax=axs[0])
    plot_acf(coronavirus_df['Deaths'],lags=20, alpha=0.2, ax=axs[1])
    plt.show()

'''REGRESSION ANALYSIS'''

import statsmodels.api as sma

coronavirus_df = sma.add_constant(coronavirus_df)
intercept_y = sma.OLS(coronavirus_df['Deaths'], coronavirus_df[['const','Recovered']]).fit()
print('Results:', intercept_y.summary())
print('Constant Coefficient:',intercept_y.params[0])
print('Independent Variable:',intercept_y.params[1])

'ADD FULLER TEST'
from statsmodels.tsa.stattools import adfuller

adfuller_test = adfuller(coronavirus_df['Deaths'])
print(adfuller_test)
print('p-value: ', adfuller_test[1])
alpha = 0.05
if adfuller_test[1] > alpha:
    print('The Null Hypothesis cant be rejected: It may not be a Random Walk(IT MAY BE PREDICTABLE)')
else:
    print('The Null Hypothesis is rejected(It is a Random Walk)')

from statsmodels.tsa.arima_process import ArmaProcess

ar = np.array([1, 0.9])
ma = np.array([1, 0.7])
AR_object = ArmaProcess(ar, ma)
Simulated_data = AR_object.generate_sample(nsample=5000)
print('This is my ARMA simulation:', Simulated_data)

from statsmodels.tsa.arima_model import ARMA

arma_model = ARMA(coronavirus_df['Confirmed'], order=(1,0))
arma_results = arma_model.fit()
print('This is my trained ARMA model:', arma_results.summary())

predict_data = arma_results.predict(start=72, end=140)
print('This is my predicted ARMA:', predict_data)
arma_results.plot_predict(start=0, end=200)
plt.show()

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

from statsmodels.tsa.arima_process import ArmaProcess

ar = np.array([1, 0,9])
ma = np.array([1])
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

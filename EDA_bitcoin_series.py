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

Blockchain_df = pd.read_csv('/Users/fer/Desktop/BlockChain_Train_csv.csv', sep=',')
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


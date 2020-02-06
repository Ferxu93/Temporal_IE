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




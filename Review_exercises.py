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


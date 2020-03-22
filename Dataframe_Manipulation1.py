import numpy as np
import pandas as pd

desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_colwidth', 100)
pd.set_option('display.max_columns', 30)
pd.set_option('display.max_rows', 30)
pd.options.display.float_format = '{:.3f}'.format

Cambridge_Analytics_df = pd.read_excel('/Users/fer/Downloads/cambridge.xlsx')
print(Cambridge_Analytics_df)

# Let´s group by exptype
exptype_df = Cambridge_Analytics_df.groupby(by=['exptype'])['exptype'].count().to_frame()
print(exptype_df)
print(type(exptype_df))

Cambridge_Analytics_df.namefix2 = 'CAMBRIDGE ANALYTICA'
print(Cambridge_Analytics_df)

Purpose_df = Cambridge_Analytics_df.groupby(by=['purpose'])['purpose'].count().to_frame()
print(Purpose_df)
#Purpose_df.to_csv('/Users/fer/Desktop/CLASES NACHO/CAMBRIDGE_ANALYTICA.csv')


"""SLICING AND FILTERING DATA FRAMES DIRECTLY AND USING LOC AND ILOC"""

df1 = Cambridge_Analytics_df[['namefix2', 'cmte_id', 'transaction_amt', 'exptype']]
print('\nDataframe1\n', df1)

df2 = Cambridge_Analytics_df.iloc[:, 3:30]
print('\n Dataframe2\n',df2)

df1.to_csv('/Users/fer/Desktop/CLASES NACHO/Set_df1.csv', sep=";")
df2.to_csv('/Users/fer/Desktop/CLASES NACHO/Set_df2.csv', sep=";")


"""JOINING AND MERGING DATAFRAMES"""

dfX = pd.merge(df1, df2, how='left', on='exptype')
print(dfX)
# IF EJEMPLO MUY MALO
# PRINT CULPA DE NACHO!

dfX_correct = pd.concat([df1, df2], axis=1)
#dfX_correct.iloc[:, 0:4] = dfX_correct.iloc[:, 0:4].rename(columns={'exptype': 'delete'}, inplace=False)
#dfX_correct = dfX_correct.drop(dfX_correct.columns[3], axis=1)
dfX_correct = dfX_correct.loc[:, ~dfX_correct.columns.duplicated()]
print(dfX_correct)

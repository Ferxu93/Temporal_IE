import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_colwidth', 100)
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 30)
pd.options.display.float_format = '{:.3f}'.format

vector = np.array([1, 20])
print('this is my vector: ', vector)
print(type(vector))

vector1 = np.arange(20)
print(vector1)
print('This is my cool vector: ', vector1)



Universities_dict = {
    'Universities': ['IE', 'IESE', 'CEU', 'ICADE', 'ESADE'],
    'Number of Students': [50000, 30000, 45000, 200000, 34598]
}

print(Universities_dict)
print(type(Universities_dict))

Universities_df = pd.DataFrame(Universities_dict)
print(Universities_df)

Flights = pd.read_csv('/Users/fer/Downloads/flights_jan08.csv')
print('\n\nFlights Dataframe:\n', Flights)
print('This is the type of the object:', type(Flights))
print('This are the columns of the dataframe', Flights.columns)
print(Flights.dtypes)
print(Flights.info())
print(Flights.describe())
print(Flights.index)
print(Flights.shape)

Flights_clear_df = Flights.dropna()
print(Flights_clear_df)

carrier_clear_s1 = Flights.CarrierDelay
print(carrier_clear_s1)
print(type(carrier_clear_s1))

carrier_clean_s2 = Flights['CarrierDelay']
print(carrier_clean_s2)
print(type(carrier_clean_s2))

carrier_clean_df = Flights[['CarrierDelay']].dropna()
print(carrier_clean_df)
print(type(carrier_clean_df))

carrier_clean_df = Flights[(Flights['Distance'] >= 600) & (Flights['Dest'] == 'OKC')]
print(carrier_clean_df)
print(type(carrier_clean_df))

# carrier_clean_df.to_csv('/Users/fer/Desktop/CLASES NACHO/carrierclean.csv') # to save on a selected foulder as csv.


lista = [567, 546, 384]
s1 = (np.e ** lista[0] / (np.e ** lista[0] + np.e ** lista[1] + np.e ** lista[2]))
s2 = (np.e ** lista[1] / (np.e ** lista[0] + np.e ** lista[1] + np.e ** lista[2]))
s3 = (np.e ** lista[2] / (np.e ** lista[0] + np.e ** lista[1] + np.e ** lista[2]))

lista_ajustada_softmax = [s1, s2, s3]
plt.plot(lista)
plt.plot(lista_ajustada_softmax)
# plt.show()

v1 = np.arange(100)
v2 = np.arange(start=0, stop=200, step=2)

v1_v2_df = pd.DataFrame(v1, columns=['V1'])
v1_v2_df['V2'] = v2
print(v1_v2_df)
print(type(v1_v2_df))
print(len(v1))
print(len(v2))
print(v1_v2_df.describe())
print(v1_v2_df.columns)

import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_colwidth', 100)
pd.set_option('display.max_columns', 30)
pd.set_option('display.max_rows', 20)
pd.options.display.float_format = '{:.3f}'.format

Absenteeism_training_df = pd.read_csv('/Users/fer/Downloads/Absenteeism_at_work_classification_training.csv', sep=';')
Absenteeism_test_df = pd.read_csv('/Users/fer/Downloads/Absenteeism_at_work_classification_test.csv', sep=';')

print('\n Absenteeism Test:\n\n',Absenteeism_test_df)
print('\n Absenteeism Training: \n\n',Absenteeism_training_df)

def zlist(list):
    typified_object = []
    for item in list:
        typified_item = (item - np.mean(list)) / np.std(list)
        typified_object.append(typified_item)
    return typified_object

edad = [8,12,14,16,20,22,24,26,42,46,60]
edad_tipificada = zlist(edad)
print('list: ', edad)
print('tipified list: ', [round(item, 2) for item in edad_tipificada])
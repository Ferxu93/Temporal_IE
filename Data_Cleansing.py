import numpy as np
import pandas as pd
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
import pandas as pd
import numpy as np

desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_colwidth', 100)
pd.set_option('display.max_columns', 30)
pd.set_option('display.max_rows', 30)
pd.options.display.float_format = '{:.3f}'.format

charity = pd.read_csv('/Users/fer/Downloads/UKCharityGrants_cleaned_filtered.csv')
print(charity)

charity = charity.fillna(0)
print('\n This is my new DF\n',charity)




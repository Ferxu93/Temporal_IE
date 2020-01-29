from time import strptime

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_colwidth', 100)
pd.set_option('display.max_columns', 30)
pd.set_option('display.max_rows', 30)
pd.options.display.float_format = '{:.3f}'.format

print("""\nCOMPANIES DICTIONARY\n""")
companies_dict = {
    'CIF': ['A12', 'B64', 'A41', 'A15'],
    'COMPANY': ['Lockeed Martin', 'Boeing', 'Thales', 'BAE'],
    'HQ' : ['Washington', 'LAX', 'Paris', 'NY']
}

companies_df = pd.DataFrame(companies_dict)
print(companies_df)
print(type(companies_df))

print("""\nCONTRACTS DICTIONARY\n""")
contracts_dict = {
    'CIF': ['A28', 'A12', 'B15', 'B84', 'A15'],
    'MAIN PROJECT': ['Delta', 'Gamma', 'Alpha', 'Omega', 'Kappa'],
    'NO. EMPLOYEES': [6000, 82000, 15000, 21000, 64000 ]

}

contracts_df = pd.DataFrame(contracts_dict)
print(type(contracts_df))
print(contracts_df)

# MERGING DATAFRAMES

print("""\nMERGING COMPANIES\n""")

companies_df = pd.merge(companies_df,contracts_df, how='left', on='CIF')
print(companies_df)

# I WANT ALL THE COMPANIES OVER 80000 EMPLOYEES AS BIG_DF AND ALL COMPANIES WITH LESS THAN 80000 EMPLOYEES
print("""\nCOMPANIES\n""")
big_df = companies_df[companies_df['NO. EMPLOYEES'] > 80000]
print(big_df)
small_df = companies_df[companies_df['NO. EMPLOYEES'] < 80000]
print(small_df)

print(companies_df)

print("""\nROWS\n""")
rows_df = companies_df.iloc[1:4, :] #selecting the 3 last rows
print(rows_df)

print("""\nROWS AND COLUMNS \n""")

rows_and_files_df = companies_df.iloc[1:4, 0:3]
print(rows_and_files_df)

print("""\nFIRST 3 ROWS AND LAST 2 COLUMNS\n""")

R_F_df = companies_df.iloc[0:3, 1:3]
print(R_F_df)

print("""\nPLAYING WITH STRINGS\n""")

CAPS = str(R_F_df).upper() # TO PUT CAPITAL LETTERS
print(CAPS)

replacement =str(R_F_df.COMPANY).replace('a', 'F') # Replacing letters or  adding phrases
print(replacement)

print("""\nLISTS AND ZIPPING LOOPS\n""")

ilist =[]
for item, item1 in zip(companies_df.COMPANY, companies_df.HQ):
    if 'i' in item:
        ilist.append(item)
    elif 'i' in item1:
        ilist.append(item1)

print(ilist)










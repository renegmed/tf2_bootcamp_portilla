import numpy as np 
import pandas as pd 

columns = ['W', 'X', 'Y', 'Z']

index = ['A', 'B', 'C', 'D', 'E']

from numpy.random import randint 

np.random.seed(42)
data = randint(-100, 100, (5,4))

print("random seed 42 generated data (5 rows x 4 cols):\n{}\n".format(data))

df = pd.DataFrame(data, index, columns)
 
print("----- current values of df:\n{}\n".format(df))
print("apply condition to df (boolean values), df > 0:\n{}\n".format(df>0))
print("apply condition to df (false = NaN), df[df > 0]:\n{}\n".format(df[df>0]))

print("----- current values of df:\n{}\n".format(df))
print("filter out X column with values > 0 and show the new table, df[df['X']>0]\n{}\n".format(df[df['X']>0]))
print("filter out X column with values > 0 and show column W only, df[df['X']>0]['W']\n{}\n".format(df[df['X']>0]['W']))
print("filter out X column with values > 0 and show row A only, df[df['X']>0].iloc[0]\n{}\n".format(df[df['X']>0].iloc[0]))

#------ combining conditions -------

print("----- current values of df:\n{}\n".format(df))
df_and = df[(df['W'] > 0) & (df['Y'] > 1)]
print("combined AND condition, df[(df['W'] > 0) & (df['Y'] > 1)]:\n{}\n".format(df_and))

print("----- current values of df:\n{}\n".format(df))
df_or = df[(df['X'] > 0) | (df['Z'] > 1)]
print("combined OR condition, df[(df['X'] > 0) | (df['Z'] > 1)]:\n{}\n".format(df_or))


# Note: States is not a column, just name of index
df_reset = df.reset_index()
print("----- current values of df_reset:\n{}\n".format(df_reset))
new_indx = ['CA', 'NY', 'WY', 'OR', 'CO']
df_reset['States'] = new_indx
print("df_reset['States'] = new_indx:\n{}\n".format(df_reset))

# Note: States is not a column, just name of index
df_reset.set_index('States')
print("df_reset.set_index('States'):\n{}\n".format(df_reset))


print("df_reset.describe():\n{}\n".format(df_reset.describe()))


print("df_reset.info():\n{}\n".format(df_reset.info()))


print("df_reset.dtypes:\n{}\n".format(df_reset.dtypes))


import numpy as np 
import pandas as pd 

columns = ['W', 'X', 'Y', 'Z']

index = ['A', 'B', 'C', 'D', 'E']

from numpy.random import randint 

np.random.seed(42)
data = randint(-100, 100, (5,4))

print("random seed 42 generated data (5 rows x 4 cols):\n{}\n".format(data))

df = pd.DataFrame(data, index, columns)

print("data with index and column labels applied, pd.DataFrame(data, index, columns):\n{}\n".format(df))

print("show type of column 'W', type(df['W']):\n{}\n".format(type(df['W'])))

print("show column 'W', df['W']:\n{}\n".format(df['W'] ))

print("show list of columns, df[['Z','W']]:\n{}\n".format(df[['Z','W']] ))

#---- create and drop new column. Useful in feature engineering -----

df['new'] = df['W'] + df['Y']
print("after adding new column, df['new'] = df['W'] + df['Y']:\n{}\n".format(df))

# axis=1 mean operate on column
df = df.drop('new', axis=1) 
print("after dropping new column, df = df.drop('new', axis=1) :\n{}\n".format(df))


#---- create and drop new row -----
print("----- current values of df:\n{}\n".format(df))
print("values of row A, df.loc['A']:\n{}\n".format(df.loc['A']))

print("----- current values of df:\n{}\n".format(df))
print("values of row A and E, df.loc[['A', 'E']]:\n{}\n".format(df.loc[['A', 'E']]))

print("----- current values of df:\n{}\n".format(df))
print("value of row index 0 (row A), df.iloc[0]:\n{}\n".format(df.iloc[0]))

print("----- current values of df:\n{}\n".format(df))
print("value of row index 1 (row B), df.iloc[1]:\n{}\n".format(df.iloc[1]))

print("----- current values of df:\n{}\n".format(df))
print("value of selected rows - A B C, df.iloc[0:3]:\n{}\n".format(df.iloc[0:3]))

# axis=0 by default
df.drop('C')


#----- get subset of rows and columns at the same time ----
print("----- current values of df:\n{}\n".format(df))
print("values from rows A and C on columns W and Y:\n{}\n".format(df.loc[['A','C'],['W','Y']]))





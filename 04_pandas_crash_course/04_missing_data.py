import numpy as np 
import pandas as pd 

df = pd.DataFrame({'A':[1,2,np.nan,4],
                    'B':[5, np.nan, np.nan, 8],
                    'C':[10, 20, 30, 40]})

print("------current df value, df:\n{}\n".format(df))

print("drop rows (default axis=0) with NaN, df.dropna():\n{}\n".format(df.dropna()))

print("------current df value, df:\n{}\n".format(df))
print("drop columns (axis=1) with at least 3 non-null-values(B has 2, A has 3), df.dropna(axis=1,thresh=3):\n{}\n".format(df.dropna(axis=1,thresh=3)))



print("------current df value, df:\n{}\n".format(df))
thresh = 0.75*len(df)
print(thresh)
print("drop columns (axis=1) with less than 25% or more non-null-values, df.dropna(axis=1,thresh=0.75*len(df):\n{}\n".format(df.dropna(axis=1,thresh=thresh)))

# ------ filling the missing data ----------
print("------current df value, df:\n{}\n".format(df))
print("fill missing values with string, df.fillna(value='FILL VALUE'):\n{}\n".format(df.fillna(value='FILL VALUE')))


print("------current df value, df:\n{}\n".format(df))
print("fill missing values with zeros, df.fillna(value=0):\n{}\n".format(df.fillna(value=0)))

print("------current df value, df:\n{}\n".format(df))
print("fill missing values with zeros on column A only, df['A'].fillna(value=0):\n{}\n".format(df['A'].fillna(value=0)))


print("------current df value, df:\n{}\n".format(df))
print("fill column B with mean value, df['B'].fillna(value=df['B'].mean()):\n{}\n".format( df['B'].fillna(value=df['B'].mean()) ) )


print("------current df value, df:\n{}\n".format(df))
print("fill mean value across dataframe, df.fillna(df.mean()):\n{}\n".format( df.fillna(df.mean()) ) )
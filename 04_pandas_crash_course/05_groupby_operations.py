import pandas as pd 

df = pd.read_csv('Universities.csv')

print("-----Universities.csv df.head():\n{}\n".format(df.head()))

#print("------ current df: \n{}\n".format(df))

print("Group by year sum, df.groupby('Year').sum():\n{}\n".format(df.groupby('Year').sum()))
print("Group by year type, type(df.groupby('Year').sum()):\n{}\n".format(type(df.groupby('Year').sum()) ) )
print("Group by year mean, df.groupby('Year').mean():\n{}\n".format(df.groupby('Year').mean()))

print("Group by year (sorted descending) sum, df.groupby('Year').sum().sort_index(ascending=False):\n{}\n".format(df.groupby('Year').sum().sort_index(ascending=False)))


#---- group by multiple column -------


print("-----Universities.csv df.head():\n{}\n".format(df.head()))
print("Multi-column groupby, df.groupby(['Year','Sector']).sum():\n{}\n".format(df.groupby(['Year','Sector']).sum() ) )

print("-----Universities.csv df.head():\n{}\n".format(df.head()))
print("Summary statistics, df.groupby('Year').describe():\n{}\n".format( df.groupby('Year').describe() ) )

print("-----Universities.csv df.head():\n{}\n".format(df.head()))
print("Summary statistics transposed, df.groupby('Year').describe().transpose():\n{}\n".format( df.groupby('Year').describe().transpose() ) )

import pandas as pd 
df_one = pd.DataFrame({'k1':['A', 'A', 'B', 'B', 'C', 'C'],
                        'col1':[100, 200, 300, 300, 400, 500],
                        'col2':['NY', 'CA', 'WA', 'WA', 'AK', 'NV']})
            
print("----- current df values. df_one:\n{}\n".format(df_one))

print("column's list of unique values , df_one['col2'].unique():\n{}\n".format( df_one['col2'].unique() ) )

print("----- current df values. df_one:\n{}\n".format(df_one))
print("column's count of unique values , df_one['k1'].nunique():\n{}\n".format( df_one['k1'].nunique() ) )

print("----- current df values. df_one:\n{}\n".format(df_one))
print("value counts per unique column entry , df_one['col2'].value_counts():\n{}\n".format( df_one['col2'].value_counts() ) )


print("----- current df values. df_one:\n{}\n".format(df_one))
print("drop all duplicates , df_one.drop_duplicates():\n{}\n".format( df_one.drop_duplicates() ) )


#------ create new columns with operation and function -------------

print("----- current df values. df_one:\n{}\n".format(df_one))
df_one['NEW'] = df_one['col1'] * 10

def grab_first_letter(state):
    return state[0]

grab_first_letter('NY')

df_one['first letter'] = df_one['col2'].apply(grab_first_letter)


def complex_letter(state):
    if state[0] == "W":
        return "Washington"
    else:
        return "Error"

df_one['col2'].apply(complex_letter)

print("----- current df values. df_one:\n{}\n".format(df_one))

#---- locate the index position of max and min values -----------

df_one['col1'].max()

df_one['col1'].idxmax()

df_one['col1'].idxmin()



print("----- current df values. df_one:\n{}\n".format(df_one))
my_map = {'A':1, 'B':2, 'C':3}
df_one['num'] = df_one['k1'].map(my_map)
# NOTE: keys should be existing values you want to map e.g. k1 'A' -> my_map 'A'

print("replace values using map func,\n my_map = 'A':1, 'B':2, 'C':3 \n df_one['num'] = df_one['k1'].map(my_map):\n{}\n".format(df_one['num']) )
 
print("----- current df values. df_one:\n{}\n".format(df_one)) 
df_one.columns = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6']

print("sort on c3 column, df_one.sort_values('c3', ascending=False):\n{}\n".format( df_one.sort_values('c3',ascending=False) ))

#------------ using dummies ---------------------

print("----- current df values. df_one:\n{}\n".format(df_one)) 
print("one-hot code for column c1, pd.get_dummies(df_one['c1']:\n{}\n".format( pd.get_dummies(df_one['c1']) ))

#------------ concatinating dataframe ---------------------

features = pd.DataFrame({'A':[100, 200, 300, 400, 500],
                         'B':[12, 13, 14, 15, 16] })

predictions = pd.DataFrame({'pred':[0, 1, 1, 0, 1]})

print("------ features:\n{}\n".format(features))

print("------ predictions:\n{}\n".format(predictions))

# join along the rows, axis=0 as default
print("join along the rows, pd.concat([features, predictions]):\n{}\n".format(pd.concat([features, predictions])))

print("join along the columns, pd.concat([features, predictions], axis=1):\n{}\n".format(pd.concat([features, predictions], axis=1)))                

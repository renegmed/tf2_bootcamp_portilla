import numpy as np 
import pandas as pd

labels = ['a', 'b', 'c']

mylist = [10,20,30]

arr = np.array([10,20,30])

d = {'a':10, 'b':20, 'c':30}

# transform to panda series
series_list = pd.Series(data=mylist, index=labels) 

print("panda series with list, pd.Series(data=mylist, index=labels):\n{}\n".format(series_list))

series_arr = pd.Series(data=mylist, index=labels) 

print("panda series with array, pd.Series(data=arr, index=labels):\n{}\n".format(series_arr))

series_dict = pd.Series(data=d, index=labels) 

print("panda series with dictionary, pd.Series(data=dict, index=labels):\n{}\n".format(series_dict))


salesQ1 = pd.Series(data=[250,450,200,150],index=['USA', 'China', 'India', 'Brazil'])
print("Sales Q1:\n{}\n".format(salesQ1))

salesQ2 = pd.Series(data=[260,500,210,100],index=['USA', 'China', 'India', 'Japan'])
print("Sales Q2:\n{}\n".format(salesQ2))

print("salesQ2:\n China {}\n USA   {}\n".format(salesQ2['China'], salesQ2[0]))

# ---- Operations betwee series. 
#      Note: Japan & Brazil NaN (will be fixed later in the course) Does no match the named index

print("salesQ1 + salesQ2:\n{}\n".format(salesQ1 + salesQ2))

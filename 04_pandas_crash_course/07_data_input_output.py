import numpy as np 
import pandas as pd 

df = pd.read_csv('example.csv')

df.to_csv('output.csv', index=False)

pd.read_csv('output.csv')
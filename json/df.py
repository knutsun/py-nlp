import pandas as pd
from pandas import DataFrame

df = pd.read_csv('data.csv')

df2 = pd.read_csv('data2.csv')


df3 = pd.concat([df,df2], axis=1)

df3.to_csv('data3.csv')

# df4= pd.read_csv('data3.csv', index_col='Dutch')
# print(df4)
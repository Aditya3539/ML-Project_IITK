import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.randn(6,4),
                index=pd.date_range('20190101',periods=6,freq='D'),
                columns=['A','B','C','D'],
                )
print("\n\nPandas Dataframe=\n",df)

#Selecting a single column,which yields a series,equivalent to df.A
print("\n\n df.A=\n",df.A)
print("\n\n df['A]=\n",df['A'])

#print First three rows
print(df['2019-01-01':'2019-01-03'])

#Selecting via[],which slices the rows.
print(df[0:3])      #print First three rows

#Selcting by Label
#For getting a cross section using a label
print("\n\n",df.loc['20190101'])

dates=pd.date_range('20190101',periods=6,freq="D")
print("\n\n",df.loc[dates[0]])

#Selecting on a multi-axis by label
print(df.loc[:,['A','D']])

print(df.loc['20190102':'20190104',['A','D']])

print(df.loc['20190102':'20190102',['A','D']])
print(df.loc['20190102',['A','D']])


print(df.iloc[3:5,0:2])
import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.randn(6,4),
                index=pd.date_range('20190101',periods=6,freq='D'),
                columns=['A','B','C','D'],
                )
print("\n\nPandas Dataframe=\n",df)
#Sorting by values
print("\n\nOriginal values:\n",df)
print("\n\nSorted Values:\n")
print(df.sort_values(by='B',ascending=True))
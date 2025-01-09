import pandas as pd
import numpy as np

#dictionary of lists
dict ={'First Score':[100,90,np.nan,95],
       'Second Score':[30,45,56,np.nan],
       'Third Score':[np.nan,40,80,99]  }

#creating a dataframe from list
df = pd.DataFrame(dict)
print(df)

#using isnull() function
df2=df.notnull()

print(df2)
print(df2.info())
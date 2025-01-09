import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings(action="ignore")

#dictionary of lists
dict ={'First Score':[100,90,np.nan,95],
       'Second Score':[30,45,56,np.nan],
       'Third Score':[np.nan,40,80,99]  }

#creating a dataframe from list
df = pd.DataFrame(dict)
#filling missing value using fillna()[na:not available]
df2=df.fillna(method='bfill')#bfill:backwar filling[Filling Next Value]

print(df)
print(df2)
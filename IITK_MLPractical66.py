#Boolean Indexing
import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.randn(6,4),
                index=pd.date_range('20190101',periods=6,freq='D'),
                columns=['A','B','C','D'],
                )
print("\n\ndf=\n",df)

print("\n\ndf.A=\n",df.A)

print("\n\ndf.A > 0=\n",df.A>0)

print("\ndf[df.A>=0]")

print(df.A>0)
print(df[df.A>=0])

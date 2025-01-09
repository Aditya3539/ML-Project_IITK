import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.randn(6,4),
                index=pd.date_range('20190101',periods=6,freq='D'),
                columns=['A','B','C','D'])
print("\n\ndf=\n",df)

print("\n\ndf.A=\n",df.A)

print("\n\ndf.A > 0=\n",df.A>0)

print("\ndf[df.A>=0]")

print(df.A>0)
print(df[df.A>=0])

#Task 1
print("Task-1\n")
print("\n\n",df[(df.B < 0)&(df.D <0)])
#Task 2
print("Task-2\n")
print("\n\n",df[df.B>df.B.mean()])
#Task 3
print("Task-3\n")
print("\n\n",df['B'][df.B>df.B.mean()])


import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.randn(6,4),
                index=pd.date_range('20190101',periods=6,freq='D'),
                columns=['A','B','C','D'],
                )

print("\n\npandas dataframe=\n",df)

print("\n\nHeadings in DataFrame:",df.columns)      #[A,B,C,D]
                                                    #0,1,2,3
print("\n\nRow Headings in DataFrame:",df.index)

print("\n\nValues in DataFrame:",df.values)

print("\n",df.columns[2:4])     #[C,D,E]

df['E']=df['A'].apply(lambda y:1 if(y>=0) else 0)
print(df)

print("\n\n")
print(df.groupby('E').size())

print("\n\npandas df.head()=\n")
print(df.head())
print(df.head(3))

print("\n\npandas df.tail()=\n",df.tail())
print("\n\npandas df.tail(3)=\n",df.tail(3))

print("\n\npandas df.sample()=\n",df.sample())      #sample()=prints random rows
print("\n\npandas df.sample(3)=\n",df.sample(3))

df['F']=df['B'].apply(lambda y:"YES" if(y>=0) else "NO")
print("\ndf=\n",df)

#Describe shows a quick statistical summary of your data only numerical data bydefault
print("\n\ndf.describe()=\n",df.describe())

print("\n\ndf.describe(include='all)=\n",df.describe(include='all'))

print("\n\ndf.T=\n",df.T)
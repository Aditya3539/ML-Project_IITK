import pandas as pd

data=pd.read_csv("employees_with_missing_data.csv")
print("\n\nOriginal data=\n",data)

#making new sata frame with dropped NA values
data2=data.dropna(axis=0,how='any')     #'any' is default for how, 0 for rows

print("\n\nFiltered Data= \n",data)

print("\nOld data frame length:",len(data))
print("\nNer data frame length:",len(data2))
print("\nNumber of rows with at least 1 NA value:",(len(data)-len(data2)))

#Since the difference is 236, there were 236 rows which have at least 1 Null value
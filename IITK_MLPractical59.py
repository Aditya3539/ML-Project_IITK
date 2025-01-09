import numpy as np
#Importing the SimpleImputer clas

from sklearn.impute import SimpleImputer
#Imputer object using the mean strategy and missing_values type for imputation
imputer = SimpleImputer(missing_values=np.nan,strategy='most_frequent')

data=np.array([[12,np.nan,34],
              [10,20,34],
               [np.nan,20,30],
               [10,20,30],
              [10,11,np.nan]])

print("Original Data:\n",data)
imputer=imputer.fit(data)       #Fitting the data to the imputer object

#Imputing the data
data2=imputer.transform(data)
print("\n\nInputed Data:\n",data2)
#NOTE:The mean or median is taken along the column of the matrix




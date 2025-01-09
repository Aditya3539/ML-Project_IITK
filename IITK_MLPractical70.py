#Data Transformation:Simplify the data without changing their relationship.

#Prepare the Data For AI/ML Algorithm

#4 Ways to Prepare the Data for AI/ML Algorithm:
    #1. Rescale data.(Custom range of MinMaxScalar)
    #2. Standardize data.
    #3. Normalize data.(0 to 1) Works row- wise
    #4. Binarize data

    #Steps of Data Transformation

    #Step- 1: Load the dataset from a URL.
    #Step- 2: Split the dataset into the input and output variables for machine learning.
    #Step- 3: Apply pre-processing transformation technique to transform only the input variables.
    #Step- 4: Summarize the data to show the change.

#1) Rescale data(custom range between 1 and 5)
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
pd.set_option('display.width',1000)
filename ="indians-diabetes.data.csv"
hnames=['preg','plas','pres','skin','test','mass','pedi','age','class']
#        0      1       2       3       4   5       6       7       8
dataframe  =  pd.read_csv(filename,names=hnames)
array= dataframe.values
#Seperate array into input and output componentrs
X = array[ : ,0:8]  #[row,cols]
Y = array[ : , 8]
scaler = MinMaxScaler(feature_range=(1,10))     #Range

#First Method
rescaledX = scaler.fit_transform(X)

#Second Method
scaler = scaler.fit(X)
rescaledX = scaler.transform(X)

#Summarize transformed data
print(rescaledX [ 0:30, :]) #[row,cols]

print( "\n\nMean of First coloumn=" , end="")
print(np.mean( rescaledX[ : , 0] ) )

print( "\n\nMean of Second coloumn=" , end="")
print (np.mean( rescaledX[ : , 1] ) )

#Step-1
#X_std = (X - X.min(axis=0)) / (X.max(axi=0) - X.min(axis=0))
#In Simple Way
# X_std = X - min(X) / max(X) - min(X)

#Step-2
# X_std = X_std * (max - min) + min
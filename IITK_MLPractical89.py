import matplotlib.pyplot as plt
import pandas as pd
from dask.dataframe.methods import values

#Importing the dataset
data = pd.read_csv('LinearRegressionPoly_Data.csv')
print(data)
print(data.shape)       #(7,2)
X = data.iloc[ :,0:1].values    #[rows,cols]
y = data.iloc[ :,1].values      #[rows,cols]
print("X.shape =",X.shape,"\n X=\n",X)
print("Y.shape =",y.shape,"\n Y=",y)
#Step:Fitting Linear Regression to the dataset
#Fitting the linear Regression model On two components X and Y.
from sklearn.linear_model import LinearRegression
lin=LinearRegression()
lin.fit(X,y)        #estimating the parameters of the model
y_dash=lin.predict(X)
plt.scatter(X,y,color='blue')
plt.scatter(X,y_dash,color='m')
plt.plot(X,y_dash,color='red')
plt.title('Linear Regression')
plt.xlabel('Engine Temperature')
plt.ylabel('Engine Pressure')
plt.show()

from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
print('X=\n',X)
print('X_poly = \n',X_poly)

lin2 = LinearRegression()
lin2.fit(X_poly,y)

plt.scatter(X,y,color='blue')
y_pred=lin2.predict(X_poly)
plt.plot(X,y_pred,color='red')
plt.title('Polynomial Regression')
plt.show()


#Predicitng a new result with Linear Regression
print("LinearRegression:",lin.predict([[110.0]]))

#Predicting a new result with Polynomial Regression
print("PolynomialRegression:",lin2.predict(poly.fit_transform([[110.0]])))
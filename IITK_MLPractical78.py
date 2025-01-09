#2. Feature Extraction with Recursive Feature Elimination (RFE)(Low to High)
#RFE is based on concept of p-value(Its outputs depends upon the choice of algorithm selection)
import warnings
warnings.filterwarnings(action="ignore")
import pandas as pd
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression     #Logistic Regression because of last feature(column) is discrete(Fixed Values)

# load data

filename = 'indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test','mass', 'pedi', 'age', 'class']

dataframe = pd.read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]

# feature extraction
rfe = RFE(estimator=LogisticRegression(), n_features_to_select=4)
fit = rfe.fit(X, Y) #Fit finds relationship between the variables
print( "Num Features: ", fit.n_features_ )
print( "Selected Features: ", fit.support_ )
print( "Feature Ranking: ", fit.ranking_ )

result = fit.transform(X)
print( "\n\n\n" , result[:30, :] )
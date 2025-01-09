#Load CSV Files with Pandas(Online Mode)
import warnings

warnings.filterwarnings(action="ignore")

import pandas
import urllib.request

pandas .set_option('display.max_rows',None)
pandas .set_option('display.max_columns',None)
pandas .set_option('display.width',1000)

hnames = ['sepal-length','sepal-width',
          'petal-length','petal-width','class']

web_path = urllib.request.urlopen("https://goo.gl/QnHW4g")
dataframe = pandas.read_csv(web_path,names=hnames)

print(dataframe.shape)
print(dataframe)


print("\n\n\n")
print(dataframe.values)


print("\n\n\n")
print(dataframe.columns)


print("\n\n\n")
print(dataframe.dtypes)


print("\n\n\n")
dataframe.info()

print("\n\n\n")
print(dataframe.describe(include="all"))
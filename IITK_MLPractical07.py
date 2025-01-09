#Load CSV Files with Pandas(Online Mode)
'''
import warnings

warnings.filterwarnings(action="ignore")

import pandas
import urllib.request

pandas .set_option('display.max_rows',None)
pandas .set_option('display.max_columns',None)
pandas .set_option('display.width',100000000000)

hnames = ["Age", "Workclass", "fnlwgt", "Education",
          "Education-Num", "Martial Status","Occupation",
          "Relationship", "Race", "Sex", "Capital Gain",
          "Capital Loss","Hours per week", "Country", "Target"]


web_path = urllib.request.urlopen("https://tinyurl.com/2hycaeuf")
dataframe = pandas.read_csv(web_path,names=hnames)

print(dataframe.shape)
print(dataframe)
'''
#Load CSV Files with Pandas(Online Mode)
import warnings

warnings.filterwarnings(action="ignore")

import pandas
import urllib.request

pandas .set_option('display.max_rows',None)
pandas .set_option('display.max_columns',None)
pandas .set_option('display.width',100)

hnames = ["Age", "Workclass", "fnlwgt", "Education", "Education-Num",
          "Martial Status","Occupation", "Relationship", "Race", "Sex",
          "Capital Gain", "Capital Loss","Hours per week", "Country", "Target"]



web_path = urllib.request.urlopen("https://tinyurl.com/bdf69xy6")
dataframe = pandas.read_csv(web_path,names=hnames)

print(dataframe.shape)
print(dataframe)
print("\n\n\n")
print(dataframe.dtypes)


print("\n\n\n")
dataframe.info()

print("\n\n\n")
print(dataframe.describe(include="all"))



#Load CSV Files with NumPy.(Online Mode)
#It can't handle text and It doesn't contain metadata(Row heading , Column heading)(Data about data)
import numpy
import urllib.request

web_path = urllib.request.urlopen("https://goo.gl/QnHW4g")
dataset = numpy.genfromtxt(web_path,delimiter=",")

print("Shape of Data from Url:", dataset.shape)
print("Format of Data Dim = ",dataset.ndim)
print(dataset)
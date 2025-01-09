#Load CSV Files with NumPy.(Offline Mode)
import numpy

filename= open('indians-diabetes.data.csv')

data = numpy.loadtxt(filename, delimiter=",")

filename.close()

print("Numpy loadtxt Size = ",data.shape)

print("Data: \n", data)

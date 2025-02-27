import numpy as np
print("---Sum by rows and by columns:---")
x = np.array([[1,2],[3,4]])
print("x = \n",x)
print("x.sum() = ",x.sum())     #10


print("x.sum(axis=0) column wise sum = ",x.sum(axis=0))         #Columns(first dimension)
#array([4,6])
print(x[:,0].sum(),x[:,1].sum())
#4,6

print("x.sum(axis=1) eow wise sum = ",x.sum(axis=1))            #rows(second dimension)
#array([3,7])
print(x[0,:].sum(),x[1,:].sum())        #3,7
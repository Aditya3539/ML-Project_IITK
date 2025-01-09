import numpy as np
arr = np.array([11,22,-33,0,44,55])

print("arr.sum() = ",arr.sum())     #This is member function
print(np.sum(arr))      #This is universal/global function
print("arr.std() = ",arr.std())
print("arr.mean() = ",arr.mean())
print("np.mran(arr) = ",np.mean(arr))
print("arr.max() = ",arr.max())
print("arr.min() = ",arr.min())
print("arr.size = ",arr.min())
print("arr.shape = ",arr.size)
print("arr.dtype = ",arr.dtype)

print("arr.nonzero() = ",arr.nonzero())
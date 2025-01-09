import numpy as np
ddarr = np.array([[1,2,3],[4,5,6]])
print("ddarr.ndim = ", ddarr.ndim)
print("ddarr.shape = ", ddarr.shape)
print("ddarr.size = ", ddarr.size)
print("len(ddarr) = " , len(ddarr))
print("ddarr.dtype = ",ddarr.dtype)

print(ddarr)
print("ddarr[0,1] = ", ddarr[0,1])              #[row-id,column-id]
print("ddarr[0] = ", ddarr[0 ])
print("ddarr[ :,0] = ", ddarr[ :,0])
print("ddarr[ :,2] = ", ddarr[ :,2])
print("ddarr[ :, ] = ", ddarr[ :, ])
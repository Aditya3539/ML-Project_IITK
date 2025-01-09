import numpy as np

res1 = np.random.rand(4)
print("\n res1 = ",res1)
#NOTE:Seed value makes the random numbers predictable & regeneratable.
#NOTE:Virtual random numbers are predictable.



np.random.seed(1)           #For Every Run It will Generates Same Value Only for same seed value
res2 = np.random.rand(4)
print("\n res2 = ",res2)


np.random.seed(0)
res3 = np.random.rand(4)
print("\n res3 = ",res3)

np.random.seed(1)
res4 = np.random.rand(4)
print("\n res4 = ",res4)
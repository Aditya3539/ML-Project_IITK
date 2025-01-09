import numpy as np
#Types of operation broadcasting:
    #1. Scaler Operation Broadcasting
    #2. Array Operation Broadcasting

n1 = np.array([4,5,6])
n2 = np.array([1,2,3])
print("n1 = ",n1)
print("n2 = ",n2)
print("n1 + n2 = ", n1 + n2)
print("n1 - n2 = ",n1 - n2)
n3 = np.array([4,5,6])
print(n1 + n3)
#NOTE:
#Shape must be the same for array operation broadcasting
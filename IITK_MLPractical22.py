import numpy as np
#Are all elements nonzero```````````````````````.all checks if all are non-zero,if there is any zero it will return False
print(np.all([1,2,3,-4]))
print(np.all([1,2,3,-4,0]))


#Is any elements non-zero`````````````````````.any checks if any in non-zero,if there is any non-zero it will return True
print(np.any([1,2,3,4]))
print(np.any([1,2,3,4,0]))
print(np.any([0,0,0,0.,0]))
print(np.any([0,0,0,0.,0,-1]))
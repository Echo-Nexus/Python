import numpy as np
arr1 = np.array([[10 ,20 ,30 ], [40 ,50 ,60]])
arr2 = np.array([120, 130])
result = arr1 + arr2
print(result)

# Solution is to use .reshape() method to change the shape of the arr2
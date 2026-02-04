import numpy as np

arr1 = np.array([10, 20])
arr2 = np.array([30, 40])

print(np.stack((arr1, arr2), axis=0))
print(np.stack((arr1, arr2), axis=1))

print(np.hstack((arr1, arr2)))
print(np.vstack((arr1, arr2)))
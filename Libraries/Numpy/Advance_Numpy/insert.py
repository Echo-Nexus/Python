import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])


arr_new = np.insert(arr, 2, 25) # name, index, value
print(arr)
print(arr_new)
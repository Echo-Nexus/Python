import numpy as np
arr = np.array([[10 ,20 ,30 ,40 ,50], [ 60 ,70 ,80 ,90 ,100]])

# Flatten gives the copy of the array in 1D
flattened_arr = arr.flatten()
print(flattened_arr)

# Ravel gives the view of the array in 1D
raveled_arr = arr.ravel()
print(raveled_arr)
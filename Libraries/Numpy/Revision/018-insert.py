import numpy as np
arr = np.array([10 ,20 ,30 ,40 ,50, 60 ,70 ,80 ,90 ,100])
new_arr = np.insert(arr, 5, 55)
print(new_arr)
print(new_arr.size)
import numpy as np
arr = np.array([[10 ,20 ,30 ,40 ,50], [60 ,70 ,80 ,90 ,100]])
new_arr = np.insert(arr, 0, [[15, 25, 35, 45, 55]], axis=0) # axis defines the dimension along which to insert the values
print(new_arr)
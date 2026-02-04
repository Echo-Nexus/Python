import numpy as np

arr = np.array([[1.3, 2.5, 3.6], [2.4, 4.5, 6.4]])
print(arr.dtype)

int_arr = arr.astype(int)
print(int_arr.dtype)

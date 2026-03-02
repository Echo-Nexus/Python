import numpy as np
arr1 = np.array([[10 ,20 ,30 ,40 ,50],[60 ,70 ,80 ,90 ,100]])
new_arr = np.delete(arr1, 0, axis=0)
print(new_arr)
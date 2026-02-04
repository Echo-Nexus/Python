import numpy as np

arr = np.array([[10, 20], [30, 40]])

print(arr)

new_arr = np.insert(arr, 2,  [[25, 27],[43,54]], axis=1 )
print(new_arr)

new_arr2 = np.insert(arr, 2, [[25, 27],[43,54]], axis=0 )
print(new_arr2)

new_arr3 = np.insert(arr, 2, [25, 27], axis=None )
print(new_arr3)
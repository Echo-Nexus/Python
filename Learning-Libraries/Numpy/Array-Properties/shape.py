import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr3d)

print(arr.size)
print(arr.ndim)
print(arr.shape)
print(arr.dtype)

print(arr3d.size)
print(arr3d.ndim)
print(arr3d.shape)
print(arr3d.dtype)



arr3 = np.array([
    [[1, 2, 3],
     [4, 5, 6]],

    [[7, 8, 9],
     [10, 11, 12]]
])

print(arr3)
print(arr3.shape)

import numpy as np

# Create a 1D array 
# arr = np.array([1,2,3,4,5])
# print(arr)

# # Create a 2D array
# arr2 = np.array([[1,2,3],[4,5,6]])
# print(arr2)

# # Create a 3D array 
# arr3 = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
# print(arr3)

# Using arrange to create an array
arr4 = np.arange(2, 100, 2)
print(arr4)

for num in arr4:
    if num == 72:
        print("Found 72!", num)
        break
    else :
        print("Not found 72", num)
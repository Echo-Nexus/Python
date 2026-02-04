# .ravel() -> view
# .flatten() -> copy

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print(arr.flatten())
print(arr.ravel())
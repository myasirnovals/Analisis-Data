import numpy as np

# 1 dimensional array
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# reshaped = arr.reshape(3, 3)
# print(reshaped)

# 2 dimensional array
arr = np.array([1,2,3])
expanded = arr[:, np.newaxis]
print(expanded)

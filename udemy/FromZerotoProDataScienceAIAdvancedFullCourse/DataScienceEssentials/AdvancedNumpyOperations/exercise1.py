import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
vector = np.array([1, 0, -1])

result_add = matrix + vector
print("Result Add: \n", result_add)

result_mul = matrix * 2
print("Result Mul: \n", result_mul)
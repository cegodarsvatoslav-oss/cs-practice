import numpy as np

# Задание 1
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype = int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3, dtype = int)

print(hours, hours.shape, hours.ndim, hours.size, hours.dtype)
print(line)
print(zeros)
print(unknown_table)
print(identity)

# Задание 2
print(hours[2], hours[-1], hours[1:5], hours[1::2], hours[::-1])

# Задание 3
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])
print(temperatures.shape, temperatures.ndim, temperatures.size, temperatures[1, 2], temperatures[0, :], temperatures[:, -1], temperatures[0:2, 1:], temperatures[0:2, 1:3], sep = "\n")

# Задание 4
matrix = np.arange(1, 26).reshape(5, 5)
print(matrix[0:3, :], matrix[3:5, :], matrix[:, 0:2], matrix[1:4, 2:5], matrix[3:5, 3:5], sep = "\n")

# Задание 5
changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1
print(changed_hours, hours, sep = "\n")
"""copy нужно, чтобы не менять исходный массив"""

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100
print(changed_matrix, matrix, sep = "\n")

# Задание 6
numbers = np.arange(0, 12)
table = numbers.reshape(3, 4)
transposed = numbers.T
print(numbers, table, transposed, sep = "\n")
import numpy as np

def make_table(rows, columns):
    return np.arange(rows*columns).reshape(rows,columns).tolist()

def rectangle(matrix, row_start, row_stop, column_start, column_stop):
    arr = np.array(matrix)
    return arr[row_start:row_stop, column_start:column_stop].tolist()

def replace_rectangle(matrix, row_start, row_stop, column_start, column_stop, value):
    arr = np.array(matrix)
    arr_copy = arr.copy()
    arr_copy[row_start:row_stop+1,column_start:column_stop+1] = value
    return arr_copy.tolist()

def matrix_vector_product(matrix, vector):
    a1 = np.array(matrix)
    a2 = np.array(vector)
    return (a1 @ a2).tolist()

def matrix_multiply(left, right):
    a1 = np.array(left)
    a2 = np.array(right)
    return (a1 @ a2).tolist()

def transpose_matrix(matrix):
    a = np.array(matrix)
    return a.T.tolist

def solve_system(matrix, vector):
    a1 = np.array(matrix)
    a2 = np.array(vector)
    x = np.linalg.solve(matrix, vector).tolist()
    return x

def tensor_channel_mean(tensor):
    arr = np.array(tensor)
    return arr.mean(axis=-1).tolist()

def point_distance(first, second):
    return np.linalg.norm(first - second)





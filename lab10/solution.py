import numpy as np

def make_table(rows, columns):
    return np.arange(rows*columns).reshape(rows,columns).tolist()

def rectangle(matrix, row_start, row_stop, column_start, column_stop):
    arr = np.array(matrix)
    return matrix[row_start:row_stop + 1, column_start:column_stop + 1]

def replace_rectangle(matrix, row_start, row_stop, column_start, column_stop, value):
    arr = np.array(matrix)
    arr_copy = arr.copy()
    arr_copy[row_start:row_stop+1,column_start:column_stop+1] = value
    return arr_copy
print(replace_rectangle([[1, 2, 3], [4, 5, 6]], 1, 2, 0, 1, -1))



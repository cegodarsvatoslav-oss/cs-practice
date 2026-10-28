import numpy as np
def  reshape_rows(values, width):
    if len(values) % width != 0:
        return []
    return np.round(np.array(values, dtype = float), 6).reshape(-1 ,width).tolist()
def block(matrix, rows, columns):
    return np.round(np.array(matrix, dtype = float), 6)[np.ix_(rows, columns)].tolist()
def column_means(matrix):
    if len(matrix) == 0:
        return []
    return np.round(np.array(matrix,dtype = float), 6).mean(axis = 0).tolist()
def  column_range(matrix, column):
    if len(matrix) == 0:
        return []
    col = np.array(matrix, dtype = float)[:, column]
    return round(max(col) - min(col), 6)


    
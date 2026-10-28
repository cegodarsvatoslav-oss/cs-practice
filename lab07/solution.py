import numpy as np
def  reshape_rows(values, width):
    if len(values) % width != 0:
        return []
    return np.round(np.array(values, dtype = float), 6).reshape(-1 ,width).tolist()
def block(matrix, rows, columns):
    return np.round(np.array(matrix, dtype = float), 6)[np.ix_(rows, columns)].tolist()


    
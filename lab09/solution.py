import numpy as np

def make_hours():
    return np.arange(0, 22, 3).tolist()

def vector_report(values):
    a = np.array(values)
    return {
        "third": a[2],
        "last": a[-1],
        "middle": a[2:6],
        "every_second": a[::2],
        "reversed": a[::-1],
    }

def  change_vector(values):
    a = np.array(values)
    copy_a = a.copy()
    copy_a[2:5] = 99
    copy_a[::2] = -1


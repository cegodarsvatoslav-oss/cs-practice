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
    return copy_a

def  cap_above(values, limit):
    a = np.array(values)
    a = a[a > limit, limit]
    return a

def celsius_to_fahrenheit(values):
    a = np.array(values)
    return a * 9/5 + 32
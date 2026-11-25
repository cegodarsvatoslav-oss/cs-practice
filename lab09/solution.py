import numpy as np

def make_hours():
    return np.arange(0, 22, 3).tolist()

def vector_report(values):
    return {
        "third": values[2],
        "last": values[-1],
        "middle": values[2:6],
        "every_second": values[::2],
        "reversed": values[::-1],
    }

def  change_vector(values):
    a = np.array(values)
    copy_a = a.copy()
    copy_a[2:5] = 99
    copy_a[::2] = -1
    return copy_a.tolist()

def  cap_above(values, limit):
    a = np.array(values)
    a[a > limit] = limit
    return a.tolist()

def celsius_to_fahrenheit(values):
    a = np.array(values)
    return (a * 9/5 + 32).tolist()
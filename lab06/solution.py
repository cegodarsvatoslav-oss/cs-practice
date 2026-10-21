def count_items(values):
    d = {}
    for i in values:
        d[i] = d.get(i, 0)+1
    return d

def unique_sorted(values):
    return sorted(set(values))

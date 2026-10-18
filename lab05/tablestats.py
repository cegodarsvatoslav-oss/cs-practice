def read_rows(lines):
    header = None
    result = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        lineparts = [p.strip() for p in line.split(',')]
        if header == None:
            header = lineparts
            continue
        if len(lineparts) != len(header):
            continue
        rowdict = dict(zip(header, lineparts))
        result.append(rowdict)
    return result


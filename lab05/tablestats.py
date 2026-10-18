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
def count_types(rows):
    counts = {}
    for row in rows:
        kind = row.get('тип')
        if kind != None:
            counts[kind] = counts.get(kind, 0) + 1
    return counts
def total_minutes(rows, kind):
    total_sum = 0
    for row in rows:
        val = row.get('минуты', '')
        val = val.replace(',', '.')
        try:
            total_sum += float(val)
        except ValueError:
            continue
    return round(total_sum, 1)
def to_csv(counts):
    lines = ['тип, количество']
    for kind in sorted(counts.keys()):
        lines.append(f'{kind}, {counts[kind]}')
    return '\n'.join(lines) + '\n'
        

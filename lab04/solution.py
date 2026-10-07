def winner(names, scores):
    max = -1
    for i in scores:
        if max < i:
            max = i
    return names[scores.index(max)]
print(winner(["Аня", "Боря", "Вика"], [7.0,   9.0,    9.0]))



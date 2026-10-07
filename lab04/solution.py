names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]
def winner(names, scores):
    return names[scores.index(max(scores))]
def average(scores):
    if len(scores) != 0:
        return round(sum(scores)/len(scores),2)
print(average(scores))



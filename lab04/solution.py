names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]
def winner(names, scores):
    return names[scores.index(max(scores))]
def average(scores):
    if len(scores) != 0:
        return round(sum(scores)/len(scores),2)
    else:
        return 0.0
def ranking(names, scores):
    b = []
    for i in range(len(names)):
        b.append([names[i], scores[i]])
    b.sort(key = lambda x: -x[1])
    return [x[0] for x in b]


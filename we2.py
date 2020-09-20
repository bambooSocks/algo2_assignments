import numpy as np

X = [1, 4, 5, 7, 9]
n = len(X)
D = np.zeros((n, n))


def dist(x, i, j):
    if i == j:
        return 1
    else:
        output = [0]
        for l in reversed(range(i+1)):
            if D[l, i] == 0:
                D[l, i] = dist(x, l, i)
            if x[i] - x[l] < x[j] - x[i]:
                output.append(D[l, i])
        return max(output) + 1


def findMaxScore(x):
    output = [0]
    i = len(x) - 1
    for l in reversed(range(i+1)):
        if D[l, i] == 0:
            D[l, i] = dist(x, l, i)
        output.append(D[l, i])
    return max(output)


print(findMaxScore(X))
print(D)

import numpy as np

x = [10, 11, 13, 16, 17, 18]
n = len(x)
D = np.zeros((n, n))


def findMaxHelper(i, j):
    if i == j:
        return 1
    else:
        output = []
        for l in reversed(range(i+1)):
            if D[l, i] == 0:
                D[l, i] = findMaxHelper(l, i)
            if x[i] - x[l] < x[j] - x[i]:
                output.append(D[l, i])
        return max(output) + 1


def findMaxScore():
    output = []
    i = len(x) - 1
    for l in reversed(range(i+1)):
        if D[l, i] == 0:
            D[l, i] = findMaxHelper(l, i)
        output.append(D[l, i])
    return max(output)


print(findMaxScore())
print(D)

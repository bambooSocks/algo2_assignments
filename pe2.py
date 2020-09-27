n = int(input())
R = []
D = []

for _ in range(n):
    R.append(list(map(int, input().split(' '))))

for _ in range(n - 1):
    D.append(list(map(int, input().split(' '))))

W = [[-1 for _ in range(n)] for _ in range(n)]


def maxWeight(i, j):
    if W[i][j] != -1:
        return W[i][j]

    if i == 0 and j == 0:
        W[i][j] = 0
    elif i == 0:
        W[i][j] = R[i][j - 1] + maxWeight(i, j - 1)
    elif j == 0:
        W[i][j] = D[i - 1][j] + maxWeight(i - 1, j)
    else:
        W[i][j] = max(R[i][j - 1] + maxWeight(i, j - 1), D[i - 1][j] + maxWeight(i - 1, j))
    return W[i][j]


print(maxWeight(n - 1, n - 1))

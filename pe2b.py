n = int(input())
R = []
D = []

for _ in range(n):
    R.append(list(map(int, input().split(' '))))

for _ in range(n - 1):
    D.append(list(map(int, input().split(' '))))

W = []

for i in range(n):
    w = []
    for j in range(n):
        if i == 0 and j == 0:
            w.append(0)
        elif i == 0:
            w.append(R[0][j - 1] + w[j - 1])
        elif j == 0:
            w.append(D[i - 1][0] + W[i - 1][0])
        else:
            w.append(max(R[i][j - 1] + w[j - 1], D[i - 1][j] + W[i - 1][j]))
    W.append(w)

print(W[n-1][n-1])

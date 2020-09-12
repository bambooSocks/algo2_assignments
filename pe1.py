
n = int(input())

raw_s = input()
raw_b = input()

given_s = list(map(int, raw_s.split(' ')))
given_b = list(map(int, raw_b.split(' ')))


def find_best_value(s, b, x):

    min_s = None
    for i in range(x):
        adj_s = s[i] + 100*(x-i)
        if min_s is None:
            min_s = adj_s
        else:
            min_s = min(min_s, adj_s)

    max_b = None
    for j in range(x, len(s)):
        adj_b = b[j] - 100 * (j - x)
        if max_b is None:
            max_b = adj_b
        else:
            max_b = max(max_b, adj_b)

    return max_b - min_s


def dac_algo(s, b):
    if len(s) == 2 or len(b) == 2:
        return b[1] - s[0] - 100
    elif len(s) <= 1 or len(b) <= 1:
        return 0

    half = len(s)//2
    best_left = dac_algo(s[0:half], b[0:half])
    best_right = dac_algo(s[half:-1], b[half:-1])

    return max(best_left, best_right, find_best_value(s, b, half))


def find_best(s, b):
    best_rec = dac_algo(s, b)
    best_lin = None
    for i, j in zip(s, b):
        if best_lin is None:
            best_lin = j-i
        else:
            best_lin = max(best_lin, j-i)

    return max(best_rec, best_lin)


print(find_best(given_s, given_b))

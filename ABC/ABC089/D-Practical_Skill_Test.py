import math
def func(h, w, d, a, query):
    imos = [0 for _ in range(h*w)]
    pos = [[0, 0] for _ in range(h*w)]
    for i in range(h):
        for j in range(w):
            pos[a[i][j]] = [i, j]
    for i in range(d):
        for j in range(math.ceil((h*w-i)/d)):
            if j == 0:
                continue
            else:
                imos[i + d * j] = imos[i + d * (j-1)]\
                                  + abs(pos[i + d * j][0] - pos[i + d * (j-1)][0])\
                                  + abs(pos[i + d * j][1] - pos[i + d * (j-1)][1])
    for i in range(len(query)):
        print(imos[query[i][1]] - imos[query[i][0]])
    return
h, w, d = [int(i) for i in input().split()]
a = [[0 for _ in range(w)] for _ in range(h)]
for i in range(h):
    a[i] = [int(i) - 1 for i in input().split()]
q = int(input())
query = [[0, 0] for _ in range(q)]
for i in range(q):
    query[i] = [int(i) - 1 for i in input().split()]
func(h, w, d, a, query)
"""
func(3, 3, 2, [[0, 3, 2], [1, 4, 6], [7, 8, 5]], [[3, 7]])
print("ans: 5\n")
func(4, 2, 3, [[2, 6], [0, 3], [4, 1], [5, 7]], [[1, 1], [1, 1]])
print("ans: 0, 0\n")
func(5, 5, 4, [[12, 24, 6, 14, 16], [15, 21, 19, 1, 8], [13, 10, 11, 0, 18], [9, 5, 22, 7, 17], [2, 20, 4, 23, 3]], [[12, 12], [1, 9], [12, 12]])
print("ans: 0, 5, 0")
"""
# print("func({}, {}, {}, {}, {})".format(h, w, d, a, query))

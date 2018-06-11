Q=int(input())
ab=[list(map(int,[i for i in input().split()])) for q in range(Q)]
print(ab)
for q in range(Q):
    ab[q] = sorted([ab[q][0], ab[q][1]])
    point = 0
print(ab)

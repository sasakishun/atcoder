r, c, k = [int(i) for i in input().split()]
s = [["0" for _ in range(c)] for _ in range(r)]
for i in range(len(s)):
    s[i][0:c] = input()

# 全てのi,j->O(500*500) x,y->O(500*500)
for i in range(r):
    for j in range(c):

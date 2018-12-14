n = int(input())
t = [int(i) for i in input().split()]

_sum = sum(t)
m = int(input())
for _ in range(m):
    p, x = [int(i) for i in input().split()]
    print(_sum + x - t[p - 1])
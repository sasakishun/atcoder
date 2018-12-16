n = int(input())
_sum = 0
for _ in range(n):
    l, r = [int(i) for i in input().split()]
    _sum += r - l + 1
print(_sum)
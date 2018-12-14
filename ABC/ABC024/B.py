n, t = [int(i) for i in input().split()]
a = [0 for _ in range(n)]
for i in range(len(a)):
    a[i] = int(input())
a.sort()
a.append(10**7)

_sum = 0
for i in range(1, len(a)):
    if a[i] < a[i-1] + t:
        _sum += a[i] - a[i-1]
    else:
        _sum += t
print(_sum)
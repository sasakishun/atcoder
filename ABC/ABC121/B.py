n, m, c = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
count = 0
for _ in range(n):
    a = [int(i) for i in input().split()]
    _sum = 0
    for i in range(len(a)):
        _sum += a[i] * b[i]
    if _sum + c > 0:
        count += 1
print(count)
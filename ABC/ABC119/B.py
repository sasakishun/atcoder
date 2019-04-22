n = int(input())
_sum = 0
for _ in range(n):
    x, u = [i for i in input().split()]
    x = float(x)
    if u == "JPY":
        _sum += x
    else:
        _sum += 380000 * x
print(_sum)
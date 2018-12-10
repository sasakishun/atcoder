n = int(input())
_max = 0
for i in range(n):
    a, b, c, d, e = [int(i) for i in input().split()]
    _max = max(_max, a + b + c + d + e*(110/900))
print(_max)
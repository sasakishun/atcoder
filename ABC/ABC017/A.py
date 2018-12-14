_sum = 0
for _ in range(3):
    s, e = [int(i) for i in input().split()]
    _sum += int(s * e / 10)
print(_sum)

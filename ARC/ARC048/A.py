a, b = [int(i) for i in input().split()]
if a < 0 and b > 0:
    print(b - a - 1)
else:
    print(b - a)
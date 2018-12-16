a, b, c, d = [int(i) for i in input().split()]
if d <= a or c >= b:
    print(0)
elif c <= a <= d:
    print(min(b, d) - a)
elif a <= c <= b:
    print(min(b, d) - c)
else:
    print(0)
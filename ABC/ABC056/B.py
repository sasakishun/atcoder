w, a, b = [int(i) for i in input().split()]
if a + w <= b:
    print(b - (a + w))
elif b + w <= a:
    print(a - (b + w))
else:
    print(0)
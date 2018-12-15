x, a, b = [int(i) for i in input().split()]
if b <= a:
    print("delicious")
elif b <= a + x:
    print("safe")
else:
    print("dangerous")
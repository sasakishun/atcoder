a, b, c, k = [int(i) for i in input().split()]

if abs(a-b) > 10**18:
    print("Unfair")
elif k % 2 == 0:
    print(a - b)
else:
    print(b - a)

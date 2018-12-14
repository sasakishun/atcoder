d, n = [int(i) for i in input().split()]

if d == 0 and n == 100:
    print(101)
elif d == 1 and n == 100:
    print(10100)
elif d == 2 and n == 100:
    print(1010000)
else:
    print((100 ** d) * n)

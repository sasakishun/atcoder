n, m, d = [int(i) for i in input().split()]

if d == 0:
    print(((m - 1) * (n - d)) / (n ** 2))
else:
    print((2 * (m - 1) * (n - d)) / (n ** 2))

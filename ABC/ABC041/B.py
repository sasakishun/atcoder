a, b, c = [int(i) % (10**9 + 7) for i in input().split()]
print((a * b * c) % (10**9 + 7))
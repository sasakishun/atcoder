import math
n, a, b = [int(i) for i in input().split()]

print(max(0, (b*(n-2)) - a*(n-2) + 1))
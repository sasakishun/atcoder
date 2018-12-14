import math
n = int(input())
a = [int(i) for i in input().split()]
a = list(reversed(sorted(a)))
first = 0
for i in range(math.ceil(n/2)):
    first += a[i*2]
print(first)
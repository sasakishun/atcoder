import math
def combinations_count(n, r):
    return math.factorial(n) \
           // (math.factorial(n - r) * math.factorial(r))

n, p = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
# print(sorted(a))
# まず偶数の袋binaryと奇数の袋nonBinaryの数を算出
binary = 0
nonBinary = 0
for i in range(n):
    if a[i] % 2 == 0:
        binary += 1
    else:
        nonBinary += 1
if p == 0:
    count = 0
    for i in range(nonBinary+1):
        if i % 2 == 0:
            count += combinations_count(nonBinary, i)
    count *= 2 ** binary
    print(count)
else:
    count = 0
    for i in range(1, nonBinary + 1):
        if i % 2 == 1:
            count += combinations_count(nonBinary, i)
    count *= 2 ** binary
    print(count)

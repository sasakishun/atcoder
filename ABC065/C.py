n, m = [int(i) for i in input().split()]

if abs(n-m) > 1:
    print(0)
    exit()
count = 1
for i in range(1, n + 1):  # n!
    count *= i
    count %= (10**9 + 7)
for i in range(1, m + 1):  # n!
    count *= i
    count %= (10 ** 9 + 7)
if n == m:
    count *= 2
print(int(count % (10**9 + 7)))
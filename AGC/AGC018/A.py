# import math
# import fractions
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
a = sorted(a)

div = a[0]
for i in range(1, n):
    div = gcd(div, a[i])

if k % div == 0 and k <= a[-1]:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")

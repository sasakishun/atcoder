import math


def factorization(n):
    R = int(n)
    s = 0
    L = []
    div = 2
    while s == 0:
        for i in range(div, R + 1):
            if n % i == 0:
                n = n / i
                div = i
                if n == 1:
                    s = 1
                L.append(i)
                break
    return L


def cmb(n, r):
    if n - r < r:
        r = n - r
    if r == 0:
        return 1
    if r == 1:
        return n;

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p;
            for k in range(p - 1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result;


"""
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def cmb(n, r, mod):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


mod = 10 ** 9 + 7  # 出力の制限
N = 10 ** 6
g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)

"""
n, m = [int(i) for i in input().split()]
div = factorization(m)
divList = []
prevDiv = 0
for i in range(len(div)):
    if div[i] == prevDiv:
        divList[-1] += 1
    else:
        divList.append(1)
        prevDiv = div[i]
count = 1
for i in range(len(divList)):
    count *= cmb(divList[i] + n - 1, divList[i])
    # count *= combinations_count(divList[i] + n - 1, divList[i])
print(count % (10 ** 9 + 7))

# 入力 : 自然数     ex) 12
# 出力 : 約数リスト ex) [2, 2, 3]
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


def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


def search(i, r):
    count = 0
    for i in range(1, 11):
        count += cmb(10, i, mod) * r
    return count


mod = 10 ** 9 + 7  # 出力の制限
N = 10 ** 5 + 10
g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)

n = 3  # int(input())
count = 1  # 両者ともに1
div = []
for i in range(1, n + 1):
    if n % i == 0:
        div += [i]
# div += factorization(n)
print(div)
prevCount = [1 for i in range(len(div))]
for i in range(1, len(div)):
    count += search(div[i], len(factorization(div[i]))) - prevCount[i-1]
    prevCount[i] = search(div[i],len(factorization(div[i])))
# print("lcm(10,{}):{}".format(i, cmb(10, i, mod)))
print(count)
# つまりPとQのどの要素の積もNより小さくなる場合の数
# n=2の時はA:PかQの片方はすべて1で片方は2が1つ以上他1,B全部1
# 約数が[a, b, c]でa,b<n, c<nなら

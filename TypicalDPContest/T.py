k, n = [int(i) for i in input().split()]
# メモリ制限が大きいので、10**9のリストを作成

# きたまさ法で解くべき

# 漸化式はa[i] = a[i-1]+a[i-2]+....+a[i-k]
# つまりk個の和
# DPというより尺取り法
a = [1 for _ in range(n)]
_sum = 0
for i in range(k):
    _sum += a[i]
for i in range(k, n):
    a[i] = _sum
    _sum -= a[i-k]
    _sum += a[i]
print(a[n-1])
print(a)
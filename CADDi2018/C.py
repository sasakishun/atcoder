import copy
n = int(input())
a = [int(i) for i in input().split()]
_a = copy.deepcopy(a)
#a[0]<a[1]<...a{n-1]とするのに必要な掛け算の回数
imos = [0 for _ in range(n)]
for i in range(1, n):
    count = 0
    while a[i] < a[i-1]:
        count += 2
        a[i] *= 4
    imos
_min = 10**10
for i in range(n):
    #a[0]からa[i]までは負となり
    #a[i+1]からa[n-1]までは正とする
    for j in range(i+1, n):

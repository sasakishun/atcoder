n = int(input())
a = [int(i) for i in input().split()]
a = list(reversed(sorted(a)))
# 2番目を最大にするとは
# 大きいものを各組に2つずつ割り振るべき
# a > b > c > dなら[[a,b][c,d]]か[[a,c][b,d]]なので
# つまり出力は大きい順に並べたうちで、上から奇数番目のNつの和
sum = 0
for i in range(2*n):
    if i % 2 == 1:
        sum += a[i]
        # print(a[i])
print(sum)

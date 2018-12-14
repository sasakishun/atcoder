n = int(input())
a = [int(i) for i in input().split()]
if sum(a) % n != 0:
    print(-1)
    exit()

ave = int(sum(a)/len(a))
# 先頭から見ていき,aveより小さいなら1つ前から数をもらう
# これを末尾まで繰り返す
count = 0
for i in range(n-1):
    if a[i] > ave:
        a[i + 1] += a[i] - ave # 超過分を隣に移行
        count += 1
    elif a[i] < ave:
        # a[i] += ave - a[i]
        a[i+1] -= ave - a[i] # 足りない分を隣からもらう
        count += 1
print(count)
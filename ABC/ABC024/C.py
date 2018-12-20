def func(l, r, s, t):
    # nつの村があり,d日間かけて移動
    # 各日では「L[i]以上r[i]」以下の街間を移動可能
    # 民族iは「s[i]->t[i]」

    # 各民族が目的地に着く最小日数を出力

    # 単純に探索してみる
    for i in range(len(s)):
        # 民族s[i]について探索
        now = s[i]
        if s[i] < t[i]:
            for j in range(len(l)):
                # 各l[j]->r[j]により進めるところまで進む
                if l[j] <= now < r[j]:
                    now = r[j]
                    if now >= t[i]:
                        print(j+1)
                        break
        elif s[i] > t[i]:
            for j in range(len(l)):
                # 各l[j]<-r[j]により進めるところまで進む
                if l[j] < now <= r[j]:
                    now = l[j]
                    if now <= t[i]:
                        print(j + 1)
                        break
        else:
            print(1)

n, d, k = [int(i) for i in input().split()]
l = [0 for _ in range(d)]
r = [0 for _ in range(d)]
for i in range(d):
    l[i], r[i] = [int(i) for i in input().split()]
s = [0 for _ in range(k)]
t = [0 for _ in range(k)]
for i in range(k):
    s[i], t[i] = [int(i) for i in input().split()]
func(l, r, s, t)
"""
n, d, k = [10, 10, 3]
l = [1, 3, 7, 5, 4, 1, 2, 1, 1, 4]
r = [5, 6, 10, 8, 4, 4, 9, 3, 1, 5]
s = [1, 2, 10]
t = [6, 7, 1]
func(l, r, s, t)
"""

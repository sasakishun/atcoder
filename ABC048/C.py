n, x = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

# 左から順にみていき、左隣のaが多いなら、自分の飴を減らす
count = 0
for i in range(1, n):
    if a[i - 1] + a[i] > x:
        # print("hit:{}".format(i))
        if a[i - 1] <= x:
            count += a[i - 1] + a[i] - x
            a[i] -= a[i - 1] + a[i] - x
        else:
            count += a[i]
            a[i] = 0
            count += a[i-1] - x
            a[i-1] = x
    # print(a)
print(count)
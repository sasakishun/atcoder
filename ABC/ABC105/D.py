n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

count = 0
tmp_mod = 0
under = 0
for i in range(n):
    tmp_mod += (i % m)
    tmp_mod %= m

    if tmp_mod % m == 0:
        count += 1
    elif tmp_mod > m:
        tmp_mod -= a[under] % m
        tmp_mod %= m
        under += 1
    print("{}-{} mod:{}".format(under, i, tmp_mod))
print(count)
n, m = [int(i) for i in input().split()]
# 2i + 3j + 4(n - i - j) == mとなる
# a, bの組み合わせを出せというだけのもの
for i in range(m+1):
    j = 2 * i + 4 * (n - i) - m
    if i >= 0 and j >= 0 and n - i - j >= 0:
        print("{} {} {}\n".format(i, j, n - i - j))
        exit()
print("-1 -1 -1\n")

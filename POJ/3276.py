import numpy as np

n = 7  # int(input())
s_tmp = "BBFBFBB"  # input()
s = [1 if i == "B" else 0 for i in s_tmp]
print("s:{}".format(s))


def search(k):
    count = 0
    shaku = [0 for i in range(n)]
    sum = 0  # 貪欲法で計算量を減らす
    start = 0
    while start < n - k + 1:
        print("st:{} sum{}:{}".format(start, sum, shaku))
        if (s[start] + sum) % 2 != 0:
            shaku[start] += 1
            sum += 1
            count += 1
        # print("start{}:{}".format(start, s))
        if start - k + 1 >= 0 \
                and shaku[start - k + 1] == 1:
            sum -= 1
        start += 1
    print("test phase")
    while start < n:
        print("st:{} sum{}:{}".format(start, sum, shaku))
        if (s[start] + sum) % 2 != 0:
            return np.Inf
        if shaku[start - k + 1] == 1:
            sum -= 1
        start += 1
    return count

min_count = n
for k in range(1, n):

    #print(search(k))
    min_count = min(min_count, search(k))
print(min_count)
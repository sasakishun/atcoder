m, n, N = [int(i) for i in input().split()]
# 「m本」から「n本」生成

count = 0
used = 0
while N > 0:
    # print("count:{} used:{} N:{}".format(count, used, N))
    count += N
    used += N
    N = 0
    if used > 0:
        N += int(used/m)*n
        used -= int(used/m)*m
print(count)
n, k = [int(i) for i in input().split()]
a = [0 for i in range(n)]
for i in range(n):
    a[i] = int(input())
    if a[i] == 0:
        print(n)
        exit()
# a = [1] + a
maxLen = 0
i = -1  # 1
j = 0  # 1
now = 1
while i < len(a) and j < len(a):
    i += 1
    while i < len(a):
        now *= a[i]
        if now <= k:
            # print("a[{}]/a[{}]:{}".format(i, j, now))
            maxLen = max(maxLen, i - j + 1)
            i += 1
            # print(i)
        else:
            break
    if j < i:
        now = int(now / a[j])
        # print("now:{} a[{}]:{}".format(now, j, a[j]))
        j += 1
print(maxLen)

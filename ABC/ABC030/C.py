n, m = [int(i) for i in input().split()]
x, y = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

i = 0
j = 0
now = 0  # 時刻
count = 0
departA = False
while i < n and j < m:
    while i < n:
        if a[i] >= now:
            now = a[i] + x
            # count += 1
            # print("a:{} to b arrive:{}".format(a[i], now))
            i += 1
            departA = True
            break
        departA = False
        i += 1
    if departA:
        while j < m:
            if b[j] >= now:
                now = b[j] + y
                count += 1
                # print("b:{} to a arrive:{}".format(b[j], now))
                j += 1
                break
            j += 1
print(count)

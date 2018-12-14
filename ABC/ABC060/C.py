n, T = [int(i) for i in input().split()]
t = [int(i) for i in input().split()]

count = 0
prevEnd = T
for i in range(1, len(t)):
    # print("prevEnd:{} count:{}".format(prevEnd, count))
    if prevEnd <= t[i]:
        count += T
    else:
        count += t[i] - t[i-1]
    prevEnd = t[i] + T
    # print("prevEnd:{} count:{}\n".format(prevEnd, count))
print(count + T)

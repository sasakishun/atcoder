n = int(input())
a = [int(i) for i in input().split()]
a.append(-1)
sequence = [0 for i in range(n+1)]
for i in range(1, n+1):
    sequence[i] = sequence[i-1] + i

count = 0
upNum = 1
for i in range(1, n+1):
    if a[i] > a[i-1]:
        upNum += 1
    else:
        count += sequence[upNum]
        upNum = 1
    # print("count:{}".format(count))
print(count)
# print(sequence)
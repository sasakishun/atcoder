d = [int(i) for i in input().split()]
j = [int(i) for i in input().split()]

count = 0
for i in range(len(d)):
    count += max(d[i], j[i])
print(count)
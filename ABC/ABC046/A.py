a = [int(i) for i in input().split()]
a.sort()
a.append(-1)
count = 1
for i in range(1, len(a) - 1):
    if a[i] != a[i-1]:
        count += 1
print(count)
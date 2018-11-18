n = int(input())
d = [0 for i in range(n)]
for i in range(n):
    d[i] = int(input())
d = sorted(d)
count = 1
for i in range(1,n):
    if d[i] > d[i-1]:
        count += 1
print(count)
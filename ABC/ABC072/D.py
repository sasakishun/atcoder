n = int(input())
p = [int(i) - 1 for i in input().split()]
count = 0
for i in range(n-1):
    if p[i] == i:
        count += 1
        p[i+1] = p[i]
if p[n-1] == n-1:
    count += 1
print(count)

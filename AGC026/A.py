n = int(input())
a = [int(i) for i in input().split()]

count = 0
for i in range(1, n):
    if a[i-1] != -1 and a[i-1]==a[i]:
        count += 1
        a[i] = -1
print(count)
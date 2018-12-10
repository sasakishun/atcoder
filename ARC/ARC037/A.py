n = int(input())
a = [int(i) for i in input().split()]

count = 0
for i in range(n):
    if a[i] < 80:
        count += 80 - a[i]
print(count)
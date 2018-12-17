n = int(input())
k = int(input())
count = 1
for _ in range(n):
    count = min(count * 2, count + k)
print(count)
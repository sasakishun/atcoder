n = int(input())
a = [0 for _ in range(n)]
for i in range(n):
    a[i] = int(input())
a.sort()
a.reverse()
for i in range(1, len(a)):
    if a[i] != a[i-1]:
        print(a[i])
        exit()
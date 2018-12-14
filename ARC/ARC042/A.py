n, m = [int(i) for i in input().split()]
a = [0 for _ in range(m)]
thread = [0 for _ in range(n + 1)]
for i in range(m):
    a[i] = int(input())

out = []
for i in reversed(range(m)):
    if thread[a[i]] == 0:
        thread[a[i]] = 1
        out.append(a[i])
for i in range(1, n+1):
    if thread[i] == 0:
        out.append(i)
for i in range(n):
    print(out[i])
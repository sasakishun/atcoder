n, x = [int(i) for i in input().split()]
m = [0 for i in range(n)]
for i in range(n):
    m[i] = int(input())
for i in range(len(m)):
    x -= m[i]
print(n + int(x / min(m)))

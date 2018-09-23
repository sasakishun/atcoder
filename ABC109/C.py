import fractions

n, start = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]

if n == 1:
    print(abs(x[0]-start))
    exit()
dist = [0 for i in range(n)]
for i in range(n):
    dist[i] = abs(start-x[i])
max_div = 1000000000
for i in range(1, n):
    max_div = min(max_div, fractions.gcd(dist[i-1], dist[i]))
print(max_div)
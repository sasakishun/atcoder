n = int(input())
a = [int(i) for i in input().split()]
imos = [a[i] for i in range(n)]
for i in range(1, n):
    imos[i] += imos[i - 1]
diff = abs(imos[-1] - 2 * a[0])
for i in range(1, n-1):
    diff = min(diff, abs(imos[-1] - 2 * imos[i]))
print(diff)
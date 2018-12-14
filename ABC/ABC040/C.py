n = int(input())
a = [int(i) for i in input().split()]

table = [10**5 for i in range(n)]
table[-1] = 0
table[-2] = abs(a[-1] - a[-2])
for i in reversed(range(n - 2)):
    table[i] = min(abs(table[i+1] + abs(a[i] - a[i+1])),
                   abs(table[i+2] + abs(a[i] - a[i+2])))
print(table[0])
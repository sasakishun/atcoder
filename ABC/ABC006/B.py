n = int(input())
if n == 1 or n == 2:
    print(0)
    exit()
if n == 3:
    print(1)
    exit()
table = [0 for _ in range(n + 1)]
table[3] = 1
for i in range(4, n+1):
    table[i] = (table[i-1] + table[i-2] + table[i-3])%10007
print(table[n] % 10007)
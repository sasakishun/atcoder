n = int(input())
table = [0 for _ in range(10**5 + 1)]
count = 0
for _ in range(n):
    a = int(input()) - 1
    if table[a] == 1:
        count += 1
    else:
        table[a] = 1
print(count)
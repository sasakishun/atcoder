n = int(input())
i = 1
table = [False for _ in range(10**6)]
while True:
    if table[n]:
        print(i)
        exit()
    else:
        table[n] = True
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    i += 1

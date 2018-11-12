def isprime(n):
    if (n == 1):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    i = 3
    while (i ** 2 <= n):
        if (n % i == 0):
            return False
        i += 2
    return True


sosuu = [False] * (10 ** 5 + 1)
for i in range(1, 10 ** 5 + 1):
    sosuu[i] = isprime(i)

like_2017 = [0] * (10 ** 5 + 1)
i = 3
while (i <= 10 ** 5):
    if (sosuu[i] & sosuu[(i + 1) // 2]):
        like_2017[i] = 1
    i += 2

ruiseki = [0] * (10 ** 5 + 2)
for i in range(1, 10 ** 5 + 2):
    ruiseki[i] = ruiseki[i - 1] + like_2017[i - 1]

table = []
for i in range(len(like_2017)):
    if like_2017[i] == 1:
        table.append(i)
print(table)
print(like_2017)
print(ruiseki)
q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    print(ruiseki[r + 1] - ruiseki[l])

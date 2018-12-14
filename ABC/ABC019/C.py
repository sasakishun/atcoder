n = int(input())
a = [int(i) for i in input().split()]

# 各a[i]が「奇数*2^k」の形にできるとき
# この奇数が何種類あるかということ
for i in range(n):
    while a[i] % (2**7) == 0:
        a[i] = int(a[i] / (2**7))
    while a[i] % (2**6) == 0:
        a[i] = int(a[i] / (2**6))
    while a[i] % (2**5) == 0:
        a[i] = int(a[i] / (2**5))
    while a[i] % 16 == 0:
        a[i] = int(a[i] / 16)
    while a[i] % 8 == 0:
        a[i] = int(a[i] / 8)
    while a[i] % 4 == 0:
        a[i] = int(a[i] / 4)
    while a[i] % 2 == 0:
        a[i] = int(a[i] / 2)
a = sorted(a)
count = 1
for i in range(1, len(a)):
    if a[i] != a[i-1]:
        count += 1
print(count)
# print(a)
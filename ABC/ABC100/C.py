n = int(input())
# a = [0 for i in range(n)]
a = [int(i) for i in input().split()]

count = 0
for i in range(n):
    while 1:
        if a[i] % 2 == 0:
            a[i] /= 2
            count += 1
        else:
            break
print(count)

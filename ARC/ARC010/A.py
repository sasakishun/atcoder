n, m, a, b = [int(i) for i in input().split()]

for i in range(m):
    if n <= a:
        n += b
    n -= int(input())
    if n < 0:
        print(i + 1)
        exit()
print("complete")
n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

for i in range(n):
    if n <= i*(k-1)+1:
        print(i)
        exit()

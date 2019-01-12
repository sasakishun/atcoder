n, q = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
a.sort()
table = []

for _ in range(q):
    x = int(input())
    print(table[x])
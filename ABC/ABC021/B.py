n = int(input())
a, b = [int(i) - 1 for i in input().split()]
k = int(input())
p = [int(i) - 1 for i in input().split()]

table = [0 for _ in range(n)]
table[a] = 1
table[b] = 1
for _p in p:
    if table[_p] == 1:
        print("NO")
        exit()
    else:
        table[_p] = 1
print("YES")
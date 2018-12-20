n, a = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]
divs = [0 for j in range(a)]
# まずAで割った余りで分類
for i in range(n):
    divs[x[i] % a] += 1
print([i for i in range(a)])
print(divs)


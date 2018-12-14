def show(divs):
    print()
    for i in divs:
        print(i)


n, a = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]
divs = [[0 for j in range(a)] for i in range(a)]
# まずAで割った余りで分類
for i in range(n):
    divs[0][x[i] % a] += 1
show(divs)


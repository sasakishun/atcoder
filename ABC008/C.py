n = int(input())
c = [0 for _ in range(n)]
for i in range(n):
    c[i] = int(input())
c = sorted(c)
sum = 0
# 自身の約数となるコインが
# いくつあるか調べる
for i in range(n):
    div = 0
    for j in range(n):
        if i != j and c[i] % c[j] == 0:
            div += 1
    # print("i:{} j:{} div:{}".format(i, j, div))
    if div % 2 == 1:
        sum += 0.5
    else:
        sum += (div + 2) / (2 * (div + 1))
print(sum)
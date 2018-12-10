n, k = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]

plus = [0]
minus = []
zeroExist = 0

for i in range(n):
    if x[i] > 0:
        plus.append(x[i])
    elif x[i] == 0:
        zeroExist = 1
    else:
        minus.append(-x[i])
minus.append(0)
minus = list(reversed(minus))

if zeroExist == 1:
    k -= 1

cost = 10**9
for i in range(k + 1):
    if i < len(plus) and k - i < len(minus):
        # print("i:{} k-i:{}".format(i, k-i))
        if i == 0 or i == k:
            cost = min(cost, plus[i] + minus[k - i])
        else:
            cost = min(cost, plus[i] + minus[k - i]
                       + min(plus[i], minus[k - i]))
            # print("{}:{}".format(i, cost))
print(cost)

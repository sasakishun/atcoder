n, q = [int(i) for i in input().split()]
table = [0 for i in range(n + 1)] # 最後は番兵
for i in range(q):
    l, r = [int(i) - 1 for i in input().split()]
    table[l] += 1
    table[r + 1] += -1

out = ""
imosCounter = 0
for i in range(n):
    # table[i] %= 2
    imosCounter += table[i]
    if imosCounter % 2 == 1:
        out += "1"
    else:
        out += "0"
print(out)
def show(target):
    for i in range(len(target)):
        print(bin(target[i])[2:].zfill(8))
    print("len:{}".format(len(target)))


n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

# ありうる部分数列を列挙
beauty = []
for i in range(n):
    for j in range(i + 1, n + 1):
        beauty.append(sum(a[i:j]))
beauty = sorted(beauty)
target = [beauty[0]]
for i in range(1, len(beauty)):
    if beauty[i] != beauty[i - 1]:
        target.append(beauty[i])
digit = 0
# print(target)
targetDigit = target[-1]
while targetDigit > 0:
    digit += 1
    targetDigit = int(targetDigit / 2)
out = 0
while digit > 0:
    target = list(reversed(sorted(target)))
    # print(digit)
    # show(target)
    count = 0
    for i in range(len(target)):
        if target[i] >> (digit - 1) == 1:
            count += 1
    if count >= k:
        out += 2 ** (digit - 1)
        i = count
        while i < len(target):
            del (target[i])

    i = 0
    while i < len(target):
        target[i] &= (1 << (digit - 1)) - 1
        if target[i] == 0:
            del (target[i])
        else:
            i += 1
    digit -= 1
    # print("out:{}".format(out))
print(out)
"""
8 4
1 1 1 1 1 1 1 1 
"""

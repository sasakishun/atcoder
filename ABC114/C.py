n = int(input())
divAble = [0 for i in range(len(str(n)))]
digit = len(str(n))
count = 0


def search(nowDigit, num, maxDigit, okList):
    if nowDigit < maxDigit:
        search(nowDigit + 1, num * 10 + 3, maxDigit, [1, okList[1], okList[2]])
        search(nowDigit + 1, num * 10 + 5, maxDigit, [okList[0], 1, okList[2]])
        search(nowDigit + 1, num * 10 + 7, maxDigit, [okList[0], okList[1], 1])
    else:
        if num <= n:
            # print("num:{}".format(num))
            global count
            if sum(okList) == 3:
                count += 1
for i in range(digit+1):
    search(0, 0, i, [0, 0, 0])
print(count)
"""
# 7, 5, 3
# nがk桁だとして
# 先頭が1,2,3,4,5,6-> 7は0～k-1つ、7,8,9なら0～kつ
if int(str(n)[0]) >= 7:
    divAble[0] += 1
elif n > 10:
        divAble[1] += 1

if int(str(n)[0]) >= 5:
    divAble[0] += 1
elif n > 10:
        divAble[1] += 1

if int(str(n)[0]) >= 3:
    divAble[0] += 1
elif n > 10:
        divAble[1] += 1

for i in range(1, len(divAble)):
    divAble[i] += divAble[i-1]

print(divAble)
if sum(divAble) == 0:
    print(0)
    exit()
count = 1
for i in range(len(divAble)):
    if divAble[i] > 0:
        count *= divAble[i]
print(count)
"""

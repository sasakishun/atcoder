n = int(input())
#tmp = n
out = ""

tmp = 1
digit = 0
while tmp < n:
    tmp *= 4
    digit += 1
number = [0 for i in range(digit)]
print(number)
tmp = n
for i in range(digit):
    if 0 < tmp % 4 < 4:
        number[i] = tmp % 4
        tmp = int(tmp / 4)

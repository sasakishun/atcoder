n = int(input())
nine = []
six = []
i = 0
for i in range(1, 100000):
    if 9 ** i < n:
        nine.append(9 ** i)
    else:
        break
for i in range(1, 100000):
    if 6 ** i < n:
        six.append(6 ** i)
    else:
        break

print(nine)
count = 0
last = n
while last >= 6:
    if nine[-1] >= six[-1]:
        tmp = nine.pop()
        if tmp < last:
            last %= tmp
            count += int(last/tmp)
    else:
        tmp = six.pop()
        if tmp < last:
            last %= tmp
            count += int(last/tmp)

print(count + last)

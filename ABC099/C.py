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

count = 0
last = n
while last >= 9:
    if nine:
        while nine[-1] > last:
            nine.pop()
    if six:
        while six[-1] > last:
            six.pop()

    if nine:
        tmp9 = nine[-1]
        num9 = int(last / tmp9)
    if six:
        tmp6 = six[-1]
        num6 = int(last / tmp6)

    if num9 < num6:
        count += num9
        last %= tmp9
        nine.pop()
    elif num9 == num6 and last % tmp9 <= last % tmp6:
        count += num9
        last %= tmp9
        nine.pop()
    else:
        count += num6
        last %= tmp6
        six.pop()


count += int(last / 6)
last %= 6
print(count + last)

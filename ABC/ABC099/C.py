n = int(input())
paySix = []
payNine = []
i = 0
while 6**i <= n:
   paySix.append(6**i)
   i += 1
i = 0
while 9**i <= n:
   payNine.append(9**i)
   i += 1

maxCount = n
sum = 0
for j in range(n+1):
    count = 0
    count6 = 0
    count9 = 0
    nine = j
    six = n - j
    for i in reversed(range(len(payNine))):
        count9 += int(nine/payNine[i])
        nine -= int(nine/payNine[i])*payNine[i]
    # print("\ndiv target:{} 9Count:{}".format(j, count9))
    for i in reversed(range(len(paySix))):
        count6 += int(six/paySix[i])
        six -= int(six/paySix[i])*paySix[i]
    # print("div target:{} 6Count:{}".format(n-j, count6))
    maxCount = min(maxCount, count9+count6)
print(maxCount)
"""
pay = [1]
i = 1
while 6**i <= n:
   pay.append(6**i)
   i += 1
i = 1
while 9**i <= n:
   pay.append(9**i)
print(i)
pay = sorted(pay)
print(len(pay))
count = 0
for i in reversed(range(len(pay))):
    # print(i)
    count += int(n/pay[i])
    n -= int(n/pay[i])*pay[i]
    if n == 0:
        print(count)
"""
""""
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
"""
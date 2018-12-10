import math

n, m = [int(i) for i in input().split()]
ret = []

i = 1
while i * i <= m:
    if m % i == 0:
        ret.append(i)
        ret.append(int(m / i))
    i += 1
#ret.append(m)
ret = sorted(ret)
#print(ret)
for i in reversed(ret):
    if i <= int(m/n):
        print(i)
        exit()

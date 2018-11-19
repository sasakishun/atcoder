import math

n = int(input())
n -= 1
c = [0 for i in range(n)]
s = [0 for i in range(n)]
f = [0 for i in range(n)]
for i in range(n):
    c[i], s[i], f[i] = [int(i) for i in input().split()]


def nextArriveTime(station, start):
    """
    print("start:{} depart:{} arrive:{}"
          .format(start,
                  s[station] + math.ceil((start - s[station]) / f[station]) * f[station],
                  s[station] + math.ceil((start - s[station]) / f[station]) * f[station] + c[i]))
    """
    # print("kf:{}".format(math.ceil((start - s[station]) / f[station]) * f[station]))
    return s[station] \
           + max(0, math.ceil((start - s[station]) / f[station])) * f[station] \
           + c[station]

for i in range(n):
    time = s[i]
    for j in range(i, n):
        time = nextArriveTime(j, time)
        # print("{}->{}:{}".format(j, j+1, nextArriveTime(j, time)))
    print(time)
print(0)

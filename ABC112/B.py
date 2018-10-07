n, T = [int(i) for i in input().split()]
c = [0 for i in range(n)]
t = [0 for i in range(n)]

min = 10000

for i in range(n):
    c[i], t[i] = [int(i) for i in input().split()]
    if t[i] <= T:
        if c[i] < min:
            min = c[i]
if min == 10000:
    print("TLE")
else:
    print(min)
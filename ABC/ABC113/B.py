n = int(input())
t, a = [int(i) for i in input().split()]
h = [int(i) for i in input().split()]

diff = 1000000
index = 0
for i in range(n):
    tmpDiff = abs(a - (t-h[i]*0.006))
    if tmpDiff < diff:
        diff = tmpDiff
        index = i
print(index+1)
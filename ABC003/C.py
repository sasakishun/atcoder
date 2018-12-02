n, k = [int(i) for i in input().split()]
r = [int(i) for i in input().split()]
r = sorted(r)
rate = 0
for i in range(len(r) - k , len(r)):
    rate = (rate + r[i])/2
print(rate)
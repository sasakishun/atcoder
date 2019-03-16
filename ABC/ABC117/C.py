n, m = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]
x.sort()
dis = []
for i in range(1, len(x)):
    dis.append(x[i] - x[i-1])
dis.sort()
_sum = sum(dis)
n = min(n-1, m-1)
print(sum(dis[:-n]))
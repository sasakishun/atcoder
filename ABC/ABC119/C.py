n, a, b, c = [int(i) for i in input().split()]
a, b, c = sorted([a, b, c])
l = []
for i in range(n):
    l.append(int(input()))
print("a:{} b:{} c:{}".format(a, b, c))

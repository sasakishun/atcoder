n, k = [int(i) for i in input().split()]
l = [int(i) for i in input().split()]
l.sort()
l.reverse()
print(sum(l[0:k]))

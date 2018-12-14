l = [int(i) for i in input().split()]
l.sort()
if l[0] == l[1] and l[1] != l[2]:
    print(l[2])
elif l[1] == l[2] and l[2] != l[0]:
    print(l[0])
elif l[2] == l[0] and l[0] != l[1]:
    print(l[1])
else:
    print(l[0])
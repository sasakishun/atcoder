n = int(input())
a = [i for i in input().split()]
outStr = []
if n % 2 == 0:
    for i in reversed(range(int(n/2))):
        outStr += [a[int(i * 2)+1]]
    for i in range(int(n/2)):
        outStr += [a[int(i*2)]]
    print(" ".join(outStr))
else:
    for i in reversed(range(int(n/2)+1)):
        outStr += [a[int(i*2)]]
    for i in range(int(n/2)):
        outStr += [a[int(i*2)+1]]
    print(" ".join(outStr))

n, m = [int(i) for i in input().split()]
a = [0 for i in range(m)]
b = [0 for i in range(m)]

s = [[0, 0] for i in range(m)]
for i in range(m):
    a[i], b[i] = [int(i) for i in input().split()]
    s[i] = [b[i], a[i]]
count = 0
s = sorted(s)
#print(s)
i = 0
pivot = -1

for i in range(m):
    if s[i][1] >= pivot:
        count += 1
        pivot = s[i][0]
        #print("i :{} piv:{}".format(i, pivot))

"""
    count += 1
    pivot = s[i][0]
    print("i :{} piv:{}".format(i, pivot))
    i += 1
    if i < m:
        while s[i][1] < pivot:
            i += 1
            print("i2:{} piv:{}".format(i, pivot))
"""
print(count)


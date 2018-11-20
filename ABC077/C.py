n = int(input())
# a:上段,b:中段,c:下段
a = sorted([int(i) for i in input().split()])
b = sorted([int(i) for i in input().split()])
c = sorted([int(i) for i in input().split()])
"""
a = [_a[0]]
for i in range(1, n):
    if _a[i] != _a[i-1]:
        a.append(_a[i])
b = [_b[0]]
for i in range(1, n):
    if _b[i] != _b[i-1]:
        b.append(_b[i])
c = [_c[0]]
for i in range(1, n):
    if _c[i] != _c[i-1]:
        c.append(_c[i])
"""
aCount = [0 for i in range(len(a))]
bCount = [0 for i in range(len(b))]
# print(a)
# print(b)
# print(c)
#まず各bに対し、選択可能なcの個数を計算O(n)
k = len(c) - 1
for j in reversed(range(len(b))):
    if j < len(b) - 1:
        bCount[j] = bCount[j+1]
    while k >= 0 and b[j] < c[k]:
        bCount[j] = len(b) - k
        # print("bCount[{}]:{}".format(j, bCount[j]))
        k -= 1
# print(bCount)
k = len(b) - 1
for j in reversed(range(len(a))):
    if j < len(a) - 1:
        aCount[j] = aCount[j+1]
    while k >= 0 and a[j] < b[k]:
        # aCount[j] = len(a) - k
        aCount[j] += bCount[k]
        # print("bCount[{}]:{}".format(j, bCount[j]))
        k -= 1
print(sum(aCount))
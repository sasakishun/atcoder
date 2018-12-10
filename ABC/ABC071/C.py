n = int(input())
a = [int(i) for i in input().split()]
a = sorted(a)
out = [0, 0]
i = n - 1
while i > 0:
    # print("a[{}]:a[i] a[{}]:{}".format(i, a[i], i-1, a[i-1]))
    if a[i] == a[i-1]:
        out[0] = a[i]
        i -= 2
        break
    i -= 1
# print(i)
while i > 0:
    if a[i] == a[i-1]:
        out[1] = a[i]
        break
    i -= 1
print(out[0] * out[1])
"""
maxSquare = 0
for i in range(n-3):
    for j in range(i+1, n-2):
        for k in range(j+1, n-1):
            for l in range(k+1, n):
                # print("i:{} j:{} k:{} l:{}".format(a[i],a[j],a[k],a[l]))
                if a[i] == a[j] and a[k] == a[l]:
                    maxSquare = max(maxSquare, a[i]*a[k])
                    # print("{}*{}*{}*{}".format(a[i], a[j], a[k], a[l]))
                elif a[i] == a[k] and a[j] == a[l]:
                    maxSquare = max(maxSquare, a[i] * a[j])
                    # print("{}*{}*{}*{}".format(a[i], a[j], a[k], a[l]))
                elif a[i] == a[l] and a[j] == a[k]:
                    maxSquare = max(maxSquare, a[i] * a[j])
                    # print("{}*{}*{}*{}".format(a[i], a[j], a[k], a[l]))
print(maxSquare)
"""
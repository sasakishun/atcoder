# n = 12
n = int(input())
# a = [757232153, 372327760, 440075441, 195848680, 354974235, 458054863, 463477172, 740174259, 615762794, 632963102, 529866931, 64991604]
a = [int(i) for i in input().split()]
# b = [74164189, 98239366, 465611891, 362739947, 147060907, 118867039, 63189252, 78303147, 501410831, 110823640, 122948912, 572905212]
b = [int(i) for i in input().split()]
c = [0 for _ in range(n)]
for i in range(n):
    c[i] = a[i] - b[i]
if sum(c) < 0:
    print(-1)
    exit()
c.sort()
count = 0
minus = 0
for i in range(n):
    if c[i] < 0:
        minus += c[i]
        count += 1
    else:
        break
for i in reversed(range(n)):
    if minus < 0:
        minus += c[i]
        count += 1
    else:
        print(count)
        exit()
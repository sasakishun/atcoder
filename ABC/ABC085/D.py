import math

n, h = [int(i) for i in input().split()]
cut = [0 for _ in range(n)]
throw = [0 for _ in range(n)]
for i in range(n):
    cut[i], throw[i] = [int(i) for i in input().split()]
cut = list(reversed(sorted(cut)))
throw = list(reversed(sorted(throw)))
count = 0
for i in range(len(throw)):
    if h > 0 and throw[i] > cut[0]:
        h -= throw[i]
        count += 1
    else:
        break
if h > 0:
    print(math.ceil(h/cut[0])+count)
else:
    print(count)
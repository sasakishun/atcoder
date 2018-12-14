n, q = [int(i) for i in input().split()]
out = [0 for _ in range(n)]

for i in range(q):
    l, r, t = [int(i) - 1 for i in input().split()]
    t += 1
    out[l:r+1] = [t for _ in range(r+1-l)]
for i in range(n):
    print(out[i])
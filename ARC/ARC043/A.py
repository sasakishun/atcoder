n, a, b = [int(i) for i in input().split()]
s = [0 for _ in range(n)]
for i in range(n):
    s[i] = int(input())
s = sorted(s)

ave = sum(s)/n
diff = s[-1] - s[0]
if diff == 0:
    print(-1)
    exit()
p = b/diff
q = a - p * ave
print("{} {}".format(p, q))
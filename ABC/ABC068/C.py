n, m = [int(i) for i in input().split()]
a = [0 for i in range(m)]
b = [0 for i in range(m)]
semiGoal = [0 for i in range(n)]
for i in range(m):
    a[i], b[i] = [int(i) - 1 for i in input().split()]
    if b[i] == n-1:
        semiGoal[a[i]] = 1
for i in range(m):
    if a[i] == 0 and semiGoal[b[i]] == 1:
        print("POSSIBLE")
        exit()
print("IMPOSSIBLE")
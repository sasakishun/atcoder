n, k = [int(i) for i in input().split()]
t = [0 for _ in range(n)]

for i in range(n):
    t[i] = int(input())

sleep = t[0] + t[1] + t[2]
if sleep < k:
    print(3)
    exit()
for i in range(3, n):
    sleep -= t[i - 3]
    sleep += t[i]
    if sleep < k:
        print(i+1)
        exit()
print("-1")
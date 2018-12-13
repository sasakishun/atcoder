n, s, t = [int(i) for i in input().split()]
w = 0
count = 0
for _ in range(n):
    a = int(input())
    w += a
    if s <= w <= t:
        count += 1
print(count)
n = int(input())
a = [int(i) for i in input().split()]

# imos法
for i in range(1, len(a)):
    a[i] += a[i-1]
a = sorted(a)
count = 0
now = 0
if a[0] == 0:
    now += 1
    count += now
for i in range(1, len(a)):
    if a[i] == a[i-1]:
        now += 1
        count += now
    else:
        now = 0
print(count)
n = int(input())
a = [int(i) for i in input().split()]
for i in range(n):
    a[i] -= i + 1
a = sorted(a)
#print(a)
pivot = a[int(n / 2)]
#print(pivot)

count = 0
for i in range(int(n / 2)):
    count -= a[i]

for i in range(int(n / 2), n):
    count += a[i]

if n % 2 == 0:
    print(count)
else:
    print(abs(count - pivot))

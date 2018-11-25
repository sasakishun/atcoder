n = int(input())
a = [int(i) for i in input().split()]
near = 10000
out = 0
average = 0
for i in range(n):
    average += a[i]
average /= n
for i in range(n):
    if abs(a[i]- average) < near:
        near = abs(a[i]-average)
        out = i
print(out)
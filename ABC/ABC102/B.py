n = int(input())
a = [int(i) for i in input().split()]

max = 0

for i in range(n):
    for j in range(n):
        if abs(a[i] - a[j]) > max:
            max = abs(a[i] - a[j])
print(max)
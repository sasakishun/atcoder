n = int(input())
a = [int(i) for i in input().split()]

sum = 0
for i in range(len(a)):
    sum += a[i]-1
print(sum)
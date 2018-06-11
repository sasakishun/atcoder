n,m,x=[int(i) for i in input().split()]
a = [int(i) for i in input().split()]

sum_0 = 0
sum_N = 0

for i in range(len(a)):
    if a[i]<x:
        sum_0 +=1
    if a[i]>x:
        sum_N+=1
print(min(sum_0, sum_N))

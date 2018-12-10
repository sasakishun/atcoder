n = int(input())
x=[int(i) for i in input().split()]
sorted_x = sorted(x)
min = sorted_x[int((n/2)-1)]
max = sorted_x[int(n/2)] 

for i in range(n):
    if x[i]<=min:
        print(max)
    else:
        print(min)

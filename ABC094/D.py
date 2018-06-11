n = int(input())
a=[int(i) for i in input().split()]
a=sorted(a)
max = a[-1]
tmp = 0
for i in range(len(a)):
    if a[i] > max/2:
        tmp=i-1
        break
if max/2-a[tmp] <= -max/2+a[tmp+1]:
    print("{} {}".format(max, a[tmp]))
else:
    print("{} {}".format(max, a[tmp+1]))
    

n,c=[int(i) for i in input().split()]
x=[0 for i in range(n)]
v=[0 for i in range(n)]
x2=[0 for i in range(n)]
v2=[0 for i in range(n)]

#right_score = [[0,0] for i in range(n)]
left = [[0,0] for i in range(n)]

for i in range(n):
    x[i],v[i] = [int(j) for j in input().split()]
    x2[-i-1] = c-x[i]
    v2[-i-1] = v[i]
    
right_sum = [0 for i in range(n)]
left_sum = [0 for i in range(n)]


index=0
sum = 0
for j in range(n):
    right_sum[0] = v[0]-x[0]
    for i in range(1,len(x)):
        right_sum[i] += v[i]-(x[i]-x[i-1])+right_sum[i-1]
    print(right_sum)
        
    left_sum[0] = v2[0]-x2[0]
    for i in range(1,len(x2)):
        left_sum[i] += v2[i]-(x2[i]-x2[i-1])+left_sum[i-1]
    print(left_sum)

    if max(right_sum) > max(left_sum):
        index = right_sum.index(max(right_sum))
        tmp = x[index]
        sum += max(right_sum)
        print("right:{}".format(index))
        del x[index]
        del v[index]
        del x2[-index-1]
        del v2[-index-1]
        for i in range(len(x)):
            x[i] -= tmp
            x2[-i-1] -= c-tmp
    else:
        index = left_sum.index(max(left_sum))
        tmp = x[index]
        print("left:{}".format(index))
        del x[-index-1]
        del v[-index-1]
        del x2[index]
        del v2[index]
        for i in range(len(x2)):
            x2[i] -= tmp
            x[-i-1] -= c-tmp

    del right_sum[0]
    del left_sum[0]
print(sum)

h, w, d = [int(i) for i in input().split()]
a = [[int(j)-1 for j in input().split()] for i in range(h)]

q = int(input())#moving num
l = [0 for i in range(q)]#start number
r = [0 for i in range(q)]#finish number

for i in range(q):
    tmp = input().split()
    l[i]=int(tmp[0])-1
    r[i]=int(tmp[1])-1
loc = [[0, 0] for i in range(h*w)]
for i in range(h):
    for j in range(w):
        loc[a[i][j]][0] = i
        loc[a[i][j]][1] = j
#print(loc)
cost = [0 for i in range(int((h*w)/d))]
#print(cost)
for i in range(1, len(cost)):
    cost[i] += abs(loc[(i+1)*d-1][0]-loc[i*d-1][0])
    cost[i] += abs(loc[(i+1)*d-1][1]-loc[i*d-1][1])
#print(cost)
for i in range(1, len(cost)):
    cost[i] += cost[i-1]
#print(cost)

for i in range(q):
    if (l[i]+1)%d==0:
        print(cost[int(r[i]/d)]-cost[int(l[i]/d)])
    else:#recite
        print(cost[int(r[i]/d)]-cost[int(l[i]/d)+1]
              +abs(loc[int(l[i]/d)][0]-loc[l[i]][0])
              +abs(loc[int(l[i]/d)][1]-loc[l[i]][1])
        )

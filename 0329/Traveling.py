n = int(input())
t=list([[0 for i in range(3)]for j in range(n)])
#print(t)
for i in range(n):
    t[i][0],t[i][1], t[i][2]=map(int, input().split())   
for i in reversed(range(1,n)):
    t[i][0]=t[i][0]-t[i-1][0]
    t[i][1]=t[i][1]-t[i-1][1]
    t[i][2]=t[i][2]-t[i-1][2]
#print(t)

flag = 0
for i in range(n):
    if (abs(t[i][1])+abs(t[i][2])-t[i][0]) %2 != 0 or (abs(t[i][1])+abs(t[i][2]))>t[i][0]:
        flag=1
if flag == 0:
    print("Yes")
else:
    print("No")
        
        
    
        



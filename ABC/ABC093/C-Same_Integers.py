a,b,c = [int(i) for i in input().split()]
num_list = sorted([a,b,c])
#print(num_list)
min = int((num_list[2]-num_list[0])/2)+int((num_list[2]-num_list[1])/2)
if (num_list[2]-num_list[0])%2==0 and(num_list[2]-num_list[1])%2==0:
    print(min)
elif (num_list[2]-num_list[0])%2!=0 and(num_list[2]-num_list[1])%2!=0:
    print(min+1)
else:
    print(min+2)
    

n = int(input())
d = list([])
for i in range(n):
    d.append(int(input()))
#print(d)

count = 0
while len(d)!=0:
    max_val = max(d)
    while max_val == max(d):
        d.remove(max_val)
        if len(d)==0:
            break
    #print(d)
    count += 1
print(count)
    
    

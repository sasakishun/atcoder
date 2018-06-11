n, a, b = map(int, input().split())

sum = 0
for i in range(1, n+1):
    #print("{}:{}".format(i, int(i/10000)%10+int(i/1000)%10+int(i/100)%10+int(i/10)%10+i%10))
    if (a <= int(i/10000)%10+int(i/1000)%10+int(i/100)%10+int(i/10)%10+i%10 and
        b >= int(i/10000)%10+int(i/1000)%10+int(i/100)%10+int(i/10)%10+i%10):
        #print("ok")
        sum += i
print(sum)
        
    
    
    

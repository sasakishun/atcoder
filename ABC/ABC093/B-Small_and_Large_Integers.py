a,b,k = [int(i) for i in input().split()]

if a+k-1<b-k+1:
    for i in range(a,a+k):
        print(i)
    for i in range(b+1-k, b+1):
        print(i)
else:
    for i in range(a,b+1):
        print(i)
        

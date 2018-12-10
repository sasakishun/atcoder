n, m = input().split()

n = int(n)
m = int(m)

if n > 1 and m > 1:
    print((n-2)*(m-2))
elif n==1 and m > 1:
    print(m-2)
elif n>1 and m==1:
    print(n-2)
else:
    print(1)
    

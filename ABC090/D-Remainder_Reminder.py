n, k = input().split()
n = int(n)
k = int(k)

count = 0
for i in range(1,n+1):
    if int(n/i)*(i-k) > 0:
        count += int(n/i)*(i-k)
        #print("{}:{}".format(i, int(n/i)*(i-k)))
    if (n % i) + 1 - k > 0:
        count += n%i+1-k
        if k==0:
            count -= 1
            #print("{}:{}".format(i,n%i-k))
        #else:
            #print("{}:{}".format(i,n%i+1-k))
print(count)

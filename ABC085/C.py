import math
n, y = [int(i) for i in input().split()]

for i in range(min(n, math.ceil(y/10000))+1):
    # print(i)
    for j in range(min(n-i,math.ceil((y-10000*i)/1000))+1):
        # print("{} {}".format(i, j))
        if int((y - 10000*i - 5000*j)/1000) == n-i-j and n-i-j >= 0:
            print("{} {} {}".format(i, j, n-i-j))
            exit()
print("-1 -1 -1")

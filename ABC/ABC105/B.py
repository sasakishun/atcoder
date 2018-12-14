import math
n = int(input())

for i in range(int(n/4) + 1):
    for j in range(int((n-4*i)/7) + 1):
        #print("4:{} 7:{} {}".format(i, j, 4*i+7*j))
        if 4*i + 7*j == n:
            if 4*i+7*j <= n:
                print("Yes")
                exit()
print("No")
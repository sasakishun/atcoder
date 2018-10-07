import math

n, m = [int(i) for i in input().split()]

I = m
s = 0
R = int(I)
L = []
while s == 0:
    for i in range(2, R + 1):
        if I % i == 0:
            I = I / i
            if I == 1:
                s = 1
            L.append(i)
            break
L.append(R)
print(L)
"""
if len(L) == 1:
    if R <= int(m/n):
        print(R)
        exit()
    #print(R, "is a prime")
else:
"""
for i in reversed(L):
    if i <= int(m/n):
        print(i)
        exit()
#print(R, L)

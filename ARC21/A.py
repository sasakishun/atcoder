import math

n = int(input())

max = 0
k = int(math.log10(n))+1
for i in range(k):
    max += 9*10**i
print(max)
if n == max:
    print(9*int(math.log10(n)+1))
else:
    print(int(n/(10**k))-1+9*(k-1))

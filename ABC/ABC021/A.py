n = int(input())
if n % 2 != 0:
    n -= 1
    print(int(n/2) + 1)
    print(1)
else:
    print(int(n/2))
for i in range(int(n/2)):
    print(2)
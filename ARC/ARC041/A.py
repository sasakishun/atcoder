x, y = [int(i) for i in input().split()]
k = int(input())

if k <= y:
    print(x + k)
else:
    print(y + x - (k - y))
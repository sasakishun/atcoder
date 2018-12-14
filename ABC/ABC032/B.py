l, h = [int(i) for i in input().split()]
n = int(input())

for _ in range(n):
    a = int(input())
    if a < l:
        print(l - a)
    elif a > h:
        print(-1)
    else:
        print(0)
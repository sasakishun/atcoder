import math

txa, tya, txb, tyb, t, v = [int(i) for i in input().split()]
n = int(input())

for i in range(n):
    x, y = [int(i) for i in input().split()]
    # [txa, tya]->[x,y]->[txb, tyb]の距離がt*v以下なら駄目
    if math.sqrt(((txa - x)**2 + (tya - y)**2)) + math.sqrt(((txb - x)**2 + (tyb - y)**2)) <= t * v:
        print("YES")
        exit()
print("NO")
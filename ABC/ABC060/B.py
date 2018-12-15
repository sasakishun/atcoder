a, b, c = [int(i) for i in input().split()]
# aの倍数の和をbで割ったあまりがc

for i in range(1, 10**5):
    if a * i % b == c:
        print("YES")
        exit()
print("NO")
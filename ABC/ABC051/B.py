k, s = [int(i) for i in input().split()]

count = 0
for x in range(k+1):
    for y in range(k+1):
        z = s - x - y
        if 0 <= z <= k:
            # print("{} {} {}".format(x, y, z))
            count += 1
print(count)
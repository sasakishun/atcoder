n = int(input())

sum = 2025
for i in range(1, 10):
    for j in range(1, 10):
        if sum - i*j == n:
            print("{} x {}".format(i, j))
# print(sum)
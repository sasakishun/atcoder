c = [[0 for j in range(3)] for i in range(3)]

for i in range(3):
    c[i] = [int(i) for i in input().split()]

for i in range(3):
    if not c[i % 3][0] - c[(i + 1) % 3][0] == \
                    c[i % 3][1] - c[(i + 1) % 3][1] == \
                    c[i % 3][2] - c[(i + 1) % 3][2]:
        print("No")
        exit()
for i in range(3):
    if not c[0][i % 3] - c[0][(i + 1) % 3] == \
                    c[1][i % 3] - c[1][(i + 1) % 3] == \
                    c[2][i % 3] - c[2][(i + 1) % 3]:
        print("No")
        exit()
print("Yes")

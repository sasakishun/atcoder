h, w = [int(i) for i in input().split()]
s = [[0 for i in range(w)] for j in range(h)]
s2 = [['.' for i in range(w + 2)] for j in range(h + 2)]

for i in range(1, h + 1):
    input_str = input()
    for j in range(1, w + 1):
        s2[i][j] = input_str[j - 1]
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if s2[i][j] == "#":
            if s2[i - 1][j] == "." and s2[i + 1][j] == "." and s2[i][j - 1] == "." and s2[i][j + 1] == ".":
                print("No")
                exit()
print("Yes")

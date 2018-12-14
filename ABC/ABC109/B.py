n = int(input())
w = [0 for i in range(n)]

for i in range(n):
    w[i] = input()
    if i > 0 and w[i-1][-1] != w[i][0]:
        print("No")
        exit()
    else:
        for j in range(i):
            if w[j] == w[i]:
                print("No")
                exit()
print("Yes")


s = input()
for i in range(int(len(s)/2)):
    # print("s[{}]:{} s[{}]:{}".format(i, s[i], -i-1, s[-i-1]))
    if s[i] != "*" and s[-i-1] != "*":
        if s[i] != s[-i-1]:
            print("NO")
            exit()
print("YES")
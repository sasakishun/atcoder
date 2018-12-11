s = input()
for i in range(int(len(s)/2)):
    if s[i] != s[-i-1]:
        print("NO")
        exit()
print("YES")
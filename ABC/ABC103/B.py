s = input()
t = input()

for i in range(len(s)):
    if t == s:
        print("Yes")
        exit()
    s = s[1:len(s)]+s[0]
    #print(s)
print("No")
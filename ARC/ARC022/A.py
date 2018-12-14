s = input()

for i in range(len(s) - 2):
    for j in range(i+1, len(s)-1):
        for k in range(j+1, len(s)):
            if (s[i] == "I" or s[i] == "i")\
                    and (s[j] == "C" or s[j] == "c")\
                    and (s[k] == "T" or s[k] == "t"):
                print("YES")
                exit()
print("NO")
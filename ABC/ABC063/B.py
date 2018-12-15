_s = input()
s = [_s[i] for i in range(len(_s))]
s.sort()
for i in range(len(s) - 1):
    if s[i] == s[i+1]:
        print("no")
        exit()
print("yes")
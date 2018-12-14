x = input()
s = input()
out = ""
for i in range(len(s)):
    notExist = True
    for j in range(len(x)):
        if s[i] == x[j]:
            notExist = False
    if notExist:
        out += s[i]
print(out)
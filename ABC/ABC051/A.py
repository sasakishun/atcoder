_s = input()
out = ""
for i in range(len(_s)):
    if _s[i] == ",":
        out += " "
    else:
        out += _s[i]
print(out)

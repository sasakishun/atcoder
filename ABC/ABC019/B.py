s = input()
s += "0"
out = ""
count = 1
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        out += str(s[i-1]) + str(count)
        count = 1
print(out)
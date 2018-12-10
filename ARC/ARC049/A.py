s = input()
a = [int(i) for i in input().split()]
out = ""
counter = 0
for i in range(len(s)):
    if counter < 4 and a[counter] == i:
        out += "\""
        counter += 1
    out += s[i]
if a[-1] == len(s):
    out += "\""
print(out)
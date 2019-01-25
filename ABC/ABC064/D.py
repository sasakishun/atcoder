n = int(input())
s = input()

left = 0
right = 0
out = ""
for i in range(len(s)):
    if s[i] == "(":
        left += 1
        out += "("
    else:
        right += 1
        out += ")"
        if right > left:
            out = "(" + out
            left += 1
while left != right:
    if right > left:
        left += 1
        out = "(" + out
    else:
        right += 1
        out += ")"
print(out)
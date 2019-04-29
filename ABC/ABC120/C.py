s = input()
one = 0
zero = 0
for i in range(len(s)):
    if s[i] == "0":
        zero += 1
    else:
        one += 1
print(len(s) - abs(one - zero))
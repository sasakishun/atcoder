s = input()
w = int(input())

str = ""

for i in range(len(s)):
    if i%w == 0:
        str += s[i]
print(str)
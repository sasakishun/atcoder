n, l = [int(i) for i in input().split()]
s = input()

tab = 1
clash = 0
for i in range(len(s)):
    if s[i] == "+":
        tab += 1
    else:
        tab -= 1
    if tab > l:
        clash += 1
        tab = 1
print(clash)
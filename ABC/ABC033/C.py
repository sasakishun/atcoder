s = input()
s += "+"
# +で分割されている部分を全て0にする
zeroExist = False
count = 0
for i in range(len(s)):
    if s[i] == "+":
        if not zeroExist:
            count += 1
        zeroExist = False
    elif s[i] == "0":
        zeroExist = True
print(count)
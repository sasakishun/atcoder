s = input()
t = input()

sList = ["" for i in range(len(s))]
tList = ["" for i in range(len(t))]
for i in range(len(s)):
    sList[i] = (ord(s[i])-ord("a"))
for i in range(len(t)):
    tList[i] = (ord(t[i])-ord("a"))
sList = sorted(sList)
tList = sorted(tList)[::-1]

for i in range(min(len(sList), len(tList))):
    if sList[i] < tList[i]:
        print("Yes")
        exit()
    elif sList[i] > tList[i]:
        print("No")
        exit()
if len(sList) < len(tList):
    print("Yes")
else:
    print("No")

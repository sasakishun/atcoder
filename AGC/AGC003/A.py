s = input()
news = [0, 0, 0, 0]
for i in range(len(s)):
    if s[i] == "N":
        news[0] += 1
    elif s[i] == "E":
        news[1] += 1
    elif s[i] == "W":
        news[2] += 1
    elif s[i] == "S":
        news[3] += 1
if news[0] > 0 and news[3] == 0:
    print("No")
    exit()
if news[0] == 0 and news[3] > 0:
    print("No")
    exit()
if news[1] > 0 and news[2] == 0:
    print("No")
    exit()
if news[1] == 0 and news[2] > 0:
    print("No")
    exit()
print("Yes")

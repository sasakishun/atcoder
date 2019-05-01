s = input()
count = 0
_max = 0
for i in range(len(s)):
    if s[i] == "A" or s[i] == "C" or s[i] == "G" or s[i] == "T":
        count += 1
        _max = max(_max, count)
    else:
        count = 0
print(_max)
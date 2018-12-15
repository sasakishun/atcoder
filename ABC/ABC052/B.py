n = int(input())
s = input()
_max = 0
count = 0
for _s in s:
    if _s == "I":
        count += 1
    else:
        count -= 1
    _max = max(_max, count)
print(_max)
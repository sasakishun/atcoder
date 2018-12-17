n = input()
n += "-"
_max = 0
count = 1
for i in range(1, len(n)):
    # print(n[i])
    if n[i] == n[i-1]:
        count += 1
    else:
        _max = max(_max, count)
        count = 1
if _max >= 3:
    print("Yes")
else:
    print("No")
s = input()
t = int(input())
u = 0
r = 0
ques = 0
for _s in s:
    if _s == "L":
        r -= 1
    elif _s == "R":
        r += 1
    elif _s == "U":
        u += 1
    elif _s == "D":
        u -= 1
    else:
        ques += 1

if t == 1:
    print(abs(u) + abs(r) + ques)
else:
    if abs(u) + abs(r) >= ques:
        print(abs(u) + abs(r) - ques)
    else: # quesであふれているとき
        print((ques - abs(u) + abs(r)) % 2)


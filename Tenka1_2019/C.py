n = int(input())
s = input()

black = [0 for _ in range(len(s) + 1)]
white = [0 for _ in range(len(s) + 1)]
for i in range(len(s)):
    if s[i] == ".":
        white[i] = 1
    else:
        black[i] = 1
for i in reversed(range(len(black)-1)):
    black[i] += black[i + 1]
    white[i] += white[i + 1]
# print(black)
# print(white)
cost = 0
_min = 10**10
for i in range(len(black)-1):
    if s[i] == "#":
        _min = min(_min, cost + white[i])
        cost += 1
    # print("i:{} cost:{} _min:{}".format(i, cost, _min))
print(min(cost, _min))
s = input()
start = -1
goal = -1
for i in range(len(s)):
    if start == -1 and s[i] == "A":
        start = i
    if s[i] == "Z":
        goal = max(goal, i)
print(goal - start + 1)
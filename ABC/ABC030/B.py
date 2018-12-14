count = 0
for _ in range(12):
    s = input()
    for j in range(len(s)):
        if s[j] == "r":
            count += 1
            break
print(count)
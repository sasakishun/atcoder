n = int(input())
s = [0 for _ in range(n)]

for i in range(len(s)):
    s[i] = input()
s.sort()
s.append("-1")
# print(s)
_max = 0
out = s[0]
count = 1
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        if count > _max:
            out = s[i-1]
            _max = count
        count = 1
print(out)
# print(_max)
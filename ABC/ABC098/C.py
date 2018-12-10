n = int(input())
S = input()
s = [0 for i in range(n)]

for i in range(n):
    if S[i] == "E":
        s[i] = 1
min = n

count = 0
for j in range(n):
    i = 0
    if i < j and s[j] == 1:
        count += 1
    elif i > j and s[j] == 0:
        count += 1
if count < min:
    min = count

for i in range(1, n):
    if s[i-1] == 0:
        count += 1
    if s[i] == 1:
        count -= 1
    if count < min:
        min = count
print(min)

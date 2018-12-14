n = int(input())
s = [input() for i in range(n)]

m = int(input())
t = [input() for i in range(m)]

for i in range(n):
    for j in range(m):
        if s[i]==t[j]:
            s[i] = ""
            t[j] = ""
#print(s)
#print(t)
max_score = 0
for i in range(n):
    if s[i]!="" and s.count(s[i])>=max_score:
        max_score = s.count(s[i])
print(max_score)

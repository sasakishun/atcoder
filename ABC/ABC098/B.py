n = int(input())
s = input()

max = 0
for k in range(n):
    alpha = ""
    for i in range(k):
        for j in range(k, n):
            if s[i] == s[j]:
                if alpha.find(s[i]) < 0:
                    alpha += s[i]
    if len(alpha) > max:
        max = len(alpha)
print(max)

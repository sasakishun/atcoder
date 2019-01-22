n = int(input())
s1 = input()
s2 = input()

count = 0
i = 0
if s1[0] == s2[0]:
    i += 1
    count = 3
else:
    count = 6
    i += 2
while i < n:
    if s1[i - 1] == s2[i - 1]:
        if s1[i] == s2[i]:
            count *= 2
            i += 1
        else:
            count *= 2
            i += 2
    else:
        if s1[i] == s2[i]:
            i += 1
        else:
            count *= 3
            i += 2
print(count % (10 ** 9 + 7))

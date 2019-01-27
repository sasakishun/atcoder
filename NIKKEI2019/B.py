n = int(input())
a = input()
b = input()
c = input()

count = 0
for i in range(n):
    if a[i] == b[i] == c[i]:
        continue
    elif a[i] != b[i]:
        if a[i] == c[i] or b[i] == c[i]:
            count += 1
        else:
            count += 2
    elif b[i] != c[i]:
        if b[i] == a[i] or c[i] == a[i]:
            count += 1
        else:
            count += 2
    elif c[i] != a[i]:
        if c[i] == b[i] or a[i] == b[i]:
            count += 1
        else:
            count += 2
print(count)
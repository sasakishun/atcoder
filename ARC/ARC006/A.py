e = [int(i) for i in input().split()]
b = int(input())
l = [int(i) for i in input().split()]

count = 0
bonus = False
for i in range(len(e)):
    for j in range(len(l)):
        if e[i] == l[j]:
            count += 1
        elif l[j] == b:
            bonus = True

if count == 6:
    print(1)
elif count == 5:
    if bonus:
        print(2)
    else:
        print(3)
elif count == 4:
    print(4)
elif count == 3:
    print(5)
else:
    print(0)
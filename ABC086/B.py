a = [i for i in input().split()]
a[0] += a[1]
i = 0
while i**2 <= int(a[0]):
    if int(a[0]) == i**2:
        print("Yes")
        exit()
    i += 1
print("No")
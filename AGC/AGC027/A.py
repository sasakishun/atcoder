n, x = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
a = sorted(a)
b = [0 for i in range(n)]
count = 0
for i in range(n):
    if x - a[i] == 0:
        count += 1
        x -= a[i]
        b[i] = 1
    elif x - a[i] > 0 and i != n-1:
        count += 1
        x -= a[i]
        b[i] = 1
    """
    else:
        if x != 0 and i == n-1:
            if count > 0:
                print(count-1)
                print("aaaaa")
                exit()
            else:
                print(0)
                exit()
        elif x == 0:
            print(count)
            exit()
        else:
            print(count)
        exit()
    print(b)
    """
print(count)
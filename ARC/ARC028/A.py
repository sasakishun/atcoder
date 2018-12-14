n, a, b = [int(i) for i in input().split()]

i = 0
while n > 0:
    # aの番
    if i % 2 == 0:
        if n <= a:
            print("Ant")
            exit()
        else:
            n -= a
    else:
        if n <= b:
            print("Bug")
            exit()
        else:
            n -= b
    i += 1

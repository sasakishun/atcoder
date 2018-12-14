_a = input()
_b = input()
_c = input()
a = [_a[i] for i in range(len(_a))]
b = [_b[i] for i in range(len(_b))]
c = [_c[i] for i in range(len(_c))]

turn = "a"
while True:
    if turn == "a":
        if len(a) == 0:
            print("A")
            exit()
        else:
            turn = a[0]
            del a[0]
    elif turn == "b":
        if len(b) == 0:
            print("B")
            exit()
        else:
            turn = b[0]
            del b[0]
    elif turn == "c":
        if len(c) == 0:
            print("C")
            exit()
        else:
            turn = c[0]
            del c[0]
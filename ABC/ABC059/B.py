a = input()
b = input()
if len(a) > len(b):
    print("GREATER")
elif len(a) < len(b):
    print("LESS")
else:
    for i in range(len(a)):
        if int(a[i]) > int(b[i]):
            print("GREATER")
            exit()
        elif int(a[i]) < int(b[i]):
            print("LESS")
            exit()
    print("EQUAL")
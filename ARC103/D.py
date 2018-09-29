n = int(input())
x = [0 for i in range(n)]
y = [0 for i in range(n)]
ok = -1
for i in range(n):
    x[i], y[i] = [int(i) for i in input().split()]
    if i == 0:
        if (x[i] % 2 == 0 and y[i] % 2 == 0) or (x[i] % 2 == 1 and y[i] % 2 == 1):
            ok = 0
        else:
            ok = 1
    else:
        if (x[i] % 2 == 0 and y[i] % 2 == 0) or (x[i] % 2 == 1 and y[i] % 2 == 1):
            if ok != 0:
                print("-1")
                exit()
        else:
            if ok != 1:
                print("-1")
                exit()
if ok == 0:
    print(22)
    print("1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1")
    for i in range(n):
        str = ["o" for i in range(22)]
        #str = "oooooooooooooooooooooo"
        if x[i] >= 0:
            for j in range(int(x[i]/2)*2):
                str[j] = "R"
            for j in range(int(x[i]/2)*2, 10):
                if j % 2 == 0:
                    str[j] = "L"
                else:
                    str[j] = "R"
        else:
            for j in range(int((-x[i])/2)*2):
                str[j] = "L"
            for j in range(int((-x[i])/2)*2, 10):
                if j % 2 == 0:
                    str[j] = "L"
                else:
                    str[j] = "R"

        if y[i] >= 0:
            for j in range(int(y[i]/2)*2):
                str[j+10] = "U"
            for j in range(int(y[i]/2)*2, 10):
                if j % 2 == 0:
                    str[j+10] = "D"
                else:
                    str[j+10] = "U"
        else:
            for j in range(int((-y[i])/2)*2):
                str[j+10] = "D"
            for j in range(int((-y[i])/2)*2, 10):
                if j % 2 == 0:
                    str[j+10] = "D"
                else:
                    str[j+10] = "U"

        if x[i] % 2 == 0 and y[i] % 2 == 0:
            str[-2] = "R"
            str[-1] = "L"
        elif x[i] % 2 == 1 and y[i] % 2 == 1:
            if x[i] > 0:
                str[-2] = "R"
            else:
                str[-2] = "L"
            if y[i] > 0:
                str[-1] = "U"
            else:
                str[-1] = "D"
        print("".join(str))
if ok == 1:
    print(21)
    print("1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1")
    for i in range(n):
        str = ["o" for i in range(21)]
        #str = "ooooooooooooooooooooo"
        if x[i] >= 0:
            for j in range(int(x[i]/2)*2):
                str[j] = "R"
            for j in range(int(x[i]/2)*2, 10):
                if j % 2 == 0:
                    str[j] = "L"
                else:
                    str[j] = "R"
        else:
            for j in range(int((-x[i])/2)*2):
                str[j] = "L"
            for j in range(int((-x[i])/2)*2, 10):
                if j % 2 == 0:
                    str[j] = "L"
                else:
                    str[j] = "R"

        if y[i] >= 0:
            for j in range(int(y[i]/2)*2):
                str[j+10] = "U"
            for j in range(int(y[i]/2)*2, 10):
                if j % 2 == 0:
                    str[j+10] = "D"
                else:
                    str[j+10] = "U"
        else:
            for j in range(int((-y[i])/2)*2):
                str[j+10] = "D"
            for j in range(int((-y[i])/2)*2, 10):
                if j % 2 == 0:
                    str[j+10] = "D"
                else:
                    str[j+10] = "U"

        if x[i] % 2 == 0 and y[i] % 2 == 1:
            if y[i] > 0:
                str[-1] = "U"
            else:
                str[-1] = "D"
        elif x[i] % 2 == 1 and y[i] % 2 == 0:
            if x[i] > 0:
                str[-1] = "R"
            else:
                str[-1] = "L"
        print("".join(str))

s = input()
s += "0000000000"
i = 0
while i < len(s):
    # print("s:[{}:] : {}".format(i, s[i:]))
    if s[i:i + 5] == "dream":
        if s[i + 5:i + 7] == "er":
            if s[i + 7] == "a":  # dream+eraだと確定
                i += 5
                continue
            else:  # dreamerと確定
                i += 7
                continue
        else:  # dreamと確定
            i += 5
            continue
    elif s[i:i+5] == "erase":  # eraseで始まる場合
        if s[i + 5] != "r":  # eraseで確定
            i += 5
            continue
        else:  # eraserで確定
            i += 6
            continue
    elif s[i:] == "0000000000":
        print("YES")
        exit()
    else:
        print("NO")
        exit()
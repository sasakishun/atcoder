s = list(input())
removed = False
removing = False
for i in range(len(s)):
    last = list("keyence")
    j = i
    while j < len(s):
        if s[j] == last[0]:
            del last[0]
            if not last:
                print("YES")
                exit()
        else:
            j += 1
            break
        j += 1
    # 残り文字がlast = enceみたいになるので
    # sの末尾がlast = enceになっていればOK
    if i == 0 and j + len(last) <= len(s) and s[len(s)-len(last):] == last:
        print("YES")
        exit()
print("NO")
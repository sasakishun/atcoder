a, b = [int(i) for i in input().split()]
s = input()

for i in range(len(s)):
    if i == a:
        if s[i] != "-":
            print("No")
            exit()
    elif not ord("0") <= ord(s[i]) <= ord("9"):
        print("No")
        exit()
print("Yes")
s = input()
t = input()
for i in range(len(s)):
    if (s[i] != t[i] and s[i] != "@" and t[i] != "@") \
            or (s[i] == "@"
                and t[i] != "a"
                and t[i] != "t"
                and t[i] != "c"
                and t[i] != "o"
                and t[i] != "d"
                and t[i] != "e"
                and t[i] != "r"
                and t[i] != "@") \
            or (t[i] == "@"
                and s[i] != "a"
                and s[i] != "t"
                and s[i] != "c"
                and s[i] != "o"
                and s[i] != "d"
                and s[i] != "e"
                and s[i] != "r"
                and s[i] != "@"):
        print("You will lose")
        exit()
print("You can win")

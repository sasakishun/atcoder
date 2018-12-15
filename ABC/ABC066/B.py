s = input()

# s[0:i+1] == s[i+1:2*(i+1)]
for i in reversed(range(len(s))):
    if 2 * i < len(s):
        # print("{} {}".format(s[:i], s[i:2 * i]))
        if s[:i] == s[i:2 * i]:
            print(2*i)
            exit()
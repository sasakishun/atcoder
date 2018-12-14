s = input()
k = int(input())

count = 0
for i in range(len(s)):
    if s[i] != "1":
        print(s[i])
        exit()
    if s[i] == "1":
        count += 1
        if count == k:
            print(s[i])
            exit()

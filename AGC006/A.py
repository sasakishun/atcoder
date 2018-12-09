n = int(input())
s = input()
t = input()

length = 2 * n
for i in range(len(s)):
    if s[i:len(s)] == t[0:len(s) - i]:
        length = min(length, i + n)
        # print("length:{}".format(i + n))
print(length)
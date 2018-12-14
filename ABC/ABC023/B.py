n = int(input())
s = input()
if n == 1 and s == "b":
    print(0)
    exit()
out = "b"
i = 1
while True:
    if i % 3 == 1:
        out = "a" + out + "c"
    elif i % 3 == 2:
        out = "c" + out + "a"
    elif i % 3 == 0:
        out = "b" + out + "b"
    if s == out:
        print(i)
        exit()
    if len(out) >= len(s):
        print(-1)
        exit()
    i += 1
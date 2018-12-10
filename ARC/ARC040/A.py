n = int(input())
r = 0
b = 0
for _ in range(n):
    s = input()
    for i in range(n):
        if s[i] == "R":
            r += 1
        elif s[i] == "B":
            b += 1
if r > b:
    print("TAKAHASHI")
elif r < b:
    print("AOKI")
else:
    print("DRAW")
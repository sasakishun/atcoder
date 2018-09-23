s = input()

if s[0] != "A":
    print("WA")
    exit()
count = 0
for i in range(2, len(s)-1):
    if s[i] == "C":
        count += 1
if count != 1:
    print("WA")
    exit()
if ord("z") < ord(s[1]) or ord(s[1]) < ord("a"):
    print("WA")
    exit()
if ord("z") < ord(s[-1]) or ord(s[-1]) < ord("a"):
    print("WA")
    exit()
print("AC")
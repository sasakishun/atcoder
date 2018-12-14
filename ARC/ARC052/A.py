s = input()
out = ""
for _s in s:
    if ord("0") <= ord(_s) <= ord("9"):
        out += _s
print(out)
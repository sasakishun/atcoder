o = input()
e = input()
out = ""
for i in range(len(o)):
    out += o[i]
    if i < len(e):
        out += e[i]
print(out)
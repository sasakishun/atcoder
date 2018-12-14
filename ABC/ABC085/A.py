n = input()
out = ""
for i in range(len(n)):
    if i == 3:
        out += "8"
    else:
        out += n[i]
print(out)
w = input()
out = ""
for i in range(len(w)):
    if w[i] != "a" and w[i] != "i" and w[i] != "u" and w[i] != "e" and w[i] != "o":
        out += w[i]
print(out)
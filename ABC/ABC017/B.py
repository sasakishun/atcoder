x = input()
i = 0
while i < len(x):
    if i < len(x) - 1 and x[i:i+2] == "ch":
        i += 2
    elif x[i] == "o" or x[i] == "k" or x[i] == "u":
        i += 1
    else:
        print("NO")
        exit()
print("YES")
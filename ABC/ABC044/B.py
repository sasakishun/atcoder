_w = input()
w = [_w[i] for i in range(len(_w))]
if len(w) % 2 == 1:
    print("No")
    exit()
w.sort()
for i in range(int(len(w)/2)):
    if w[i*2] != w[i*2+1]:
        print("No")
        exit()
print("Yes")
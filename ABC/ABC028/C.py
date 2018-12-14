a = [int(i) for i in input().split()]
a = sorted(a)
out = []
for i in range(3):
    for j in range(i+1, 4):
        for k in range(j+1, 5):
            out.append(a[i] + a[j] + a[k])
out = sorted(out)
count = 1
for i in reversed(range(len(out) - 1)):
    if out[i] != out[i+1]:
        count += 1
        if count == 3:
            print(out[i])
            exit()
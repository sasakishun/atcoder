def search(n):
    for i in range(1, 3*n):
        if i*(i-1) == 2*n:
            return i
    return 0


n = int(input())

nodes = search(n)
if nodes != 0:
    print("Yes")
    print(nodes)
    out = [[] for i in range(nodes)]
    index = [int(i) for i in range(nodes)]
    counter = 1
    for i in range(len(index)):
        for j in range(index[i]):
            out[j].append(counter)
            out[i].append(counter)
            counter += 1
    for i in range(len(out)):
        str1 = str(out[i])
        table = str1.maketrans({
            ',': '',
            '[': '',
            ']': '',
        })
        str1 = str1.translate(table)
        print(("{} {}".format(len(out[i]), str1)))
else:
    print("No")
import math

t = int(input())
a = [0 for i in range(t)]
b = [0 for i in range(t)]
c = [0 for i in range(t)]
d = [0 for i in range(t)]


def search(A, B, C, D, table):
    # print("\n{}:{}:{}:{}".format(A, B, C, D))
    if (A - C) % B == 0:
        # print(int(((A - C) / B - 1) * B))
        A -= int(((A - C) / B - 1) * B)
    else:
        # print("round:{}".format(math.ceil((A - C) / B)))
        A -= (math.ceil((A - C) / B) - 1) * B
    # print("{}:{}:{}:{}".format(A, B, C, D))
    # print(table)
    if table[A] != 0:
        print("Yes")
        return
    elif A - B >= 0:
        table[A] = 1
        A -= B
        # print(table)
        search(A + int((C + 1 - A) / D) * D, B, C, D, table)
    else:
        print("No")
        return


for i in range(t):
    a[i], b[i], c[i], d[i] = [int(i) for i in input().split()]
for i in range(t):
    if b > d:
        print("No")
    else:
        table = [0 for i in range(b[i] + c[i] + 1)]
        search(a[i], b[i], c[i], d[i], table)

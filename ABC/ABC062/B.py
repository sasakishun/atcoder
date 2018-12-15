h, w = [int(i) for i in input().split()]
a = [["#" for _ in range(w+2)] for _ in range(h+2)]
print("".join(["#" for _ in range(w+2)]))
for _ in range(h):
    print("#{}#".format(input()))
print("".join(["#" for _ in range(w+2)]))

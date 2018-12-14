n, a, b = [int(i) for i in input().split()]
position = 0
for _ in range(n):
    s, d = [i for i in input().split()]
    if s == "East":
        position += min(b, max(a, int(d)))
    else:
        position -= min(b, max(a, int(d)))
if position > 0:
    print("East {}".format(position))
elif position < 0:
    print("West {}".format(-position))
else:
    print(0)
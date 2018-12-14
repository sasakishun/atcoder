n = int(input())
a = [int(i) for i in input().split()]

color = [0 for i in range(9)]
for i in range(n):
    if a[i] < 3200:
        color[int(a[i] / 400)] = 1
    else:
        color[-1] += 1
# print(color[0:-1])
# print(color)
print("{} {}".format(
    max(sum(color[0:-1]), min(1, color[-1])),
    sum(color[0:-1])+color[-1]))

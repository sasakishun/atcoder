n = int(input())
r = input()
_sum = 0
for i in range(n):
    if r[i] == "A":
        _sum += 4
    elif r[i] == "B":
        _sum += 3
    elif r[i] == "C":
        _sum += 2
    elif r[i] == "D":
        _sum += 1
print(_sum/n)
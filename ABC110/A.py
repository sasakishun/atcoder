a, b, c = [int(i) for i in input().split()]

n = [a, b, c]
n = sorted(n)

print(n[2]*10+n[1]+n[0])
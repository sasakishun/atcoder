a, b, c, k = [int(i) for i in input().split()]
s, t = [int(i) for i in input().split()]

if s + t >= k:
    print((a-c) * s + (b-c) * t)
else:
    print(a * s + b * t)

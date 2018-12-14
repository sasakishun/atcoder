n, a, b = [int(i) for i in input().split()]

if n >= 5:
    print(b*5 + (n-5)*a)
else:
    print(n*b)
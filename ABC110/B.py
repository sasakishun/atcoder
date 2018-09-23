n, m, X, Y = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]

if max(x) < min(y) and X < min(y) and Y > max(x) and X < Y:
    print("No War")
    exit()
else:
    print("War")
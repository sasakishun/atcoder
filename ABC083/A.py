a, b, c, d = [int(i) for i in input().split()]
if a+b > c+d:
    print("Left")
elif a+b < c+d:
    print("Right")
else:
    print("Balanced")
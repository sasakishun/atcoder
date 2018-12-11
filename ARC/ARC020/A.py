a, b = [int(i) for i in input().split()]

if abs(a) < abs(b):
    print("Ant")
elif abs(a) > abs(b):
    print("Bug")
else:
    print("Draw")
a, b = [int(i) for i in input().split()]

if a < 0 and b < 0:
    if (b - a + 1) % 2 == 0:
        print("Positive")
    else:
        print("Negative")
elif a > 0 and b > 0:
    print("Positive")
else:
    print("Zero")

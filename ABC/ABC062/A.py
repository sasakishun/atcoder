x, y = [int(i) for i in input().split()]
if x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12:
    if y == 1 or y == 3 or y == 5 or y == 7 or y == 8 or y == 10 or y == 12:
        print("Yes")
    else:
        print("No")
elif x == 4 or x == 6 or x == 9 or x == 11:
    if y == 4 or y == 6 or y == 9 or y == 11:
        print("Yes")
    else:
        print("No")
else:
    if y == 2:
        print("Yes")
    else:
        print("No")
a = int(input())
b = int(input())
c = int(input())

if a == max(a, b, c):
    print(1)
elif a == min(a, b, c):
    print(3)
else:
    print(2)

if b == max(a, b, c):
    print(1)
elif b == min(a, b, c):
    print(3)
else:
    print(2)

if c == max(a, b, c):
    print(1)
elif c == min(a, b, c):
    print(3)
else:
    print(2)
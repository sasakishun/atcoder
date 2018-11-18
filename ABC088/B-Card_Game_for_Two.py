n = input()
a = [int(i) for i in input().split()]
a = sorted(a)
alice = 0
bob = 0
for i in range(len(a)):
    if i % 2 == 0:
        alice += a[-i-1]
    else:
        bob += a[-i- 1]
print(alice-bob)
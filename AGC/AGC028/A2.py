import fractions


def lcm(x, y):
    return int((x * y) // fractions.gcd(x, y))

n, m = [int(i) for i in input().split()]
s = input()
t = input()

span = fractions.gcd(n, m)
for i in range(span):
    if s[int(n/span)*i] != t[int(m/span)*i]:
        print("-1")
        exit()
print(lcm(n, m))
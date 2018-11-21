def gcd(a, b):
    while b > 0:
        tmp = a
        a = b
        b = tmp % b
    return a


def lcm(a, b):
    tmp = gcd(a, b)
    return int((a/tmp) * b)


n = int(input())
t = [0 for i in range(n)]
for i in range(n):
    t[i] = int(input())
t = sorted(t)
sum = t[0]
for i in range(1, n):
    # print("sum:{} t:{} lcm:{}".format(sum, t, lcm(sum, t)))
    sum = lcm(sum, t[i])
    # print(sum)
print(sum)

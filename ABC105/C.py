import math

# print("{}/{}={} %{}".format(-123, 10, -123/10, -123 %10))
n = int(input())
if n == 0:
    print(0)
    exit()
out = ""
i = 0
while n != 0:
    if n % -2 != 0:
        out = str(- (n % -2)) + out
        # print("n:{} div:{}=(-2)^{}".format(n, (-2) ** i, i))
    else:
        out = str(- (n % -2)) + out

    # 12 -> 2 + 10^1, -12 -> 8 + 2*(-10)^1
    if n > 0:
        n = int(n / (-2))
    else:
        n = math.ceil(n / (-2))
    i += 1
print(out)

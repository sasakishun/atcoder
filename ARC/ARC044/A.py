def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def func(n):
    if n == 1:
        return "Not Prime"
    elif is_prime(n):
        return "Prime"
    else:
        # 素数っぽいか判定
        _n = str(n)
        if int(_n[-1]) % 2 == 0 or _n[-1] == "5":
            return "Not Prime"
            return
        _sum = 0
        for i in _n:
            _sum += int(i)
        if _sum % 3 != 0:
            return "Prime"
        else:
            return "Not Prime"
# for i in range(50):
    # print("i:{} {}".format(i, func(i)))
print(func(int(input())))

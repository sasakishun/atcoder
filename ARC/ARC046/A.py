def func(n):
    digit = int(n / 9)
    number = n - 9 * int(n/9) + 1
    out = ""
    for i in range(digit+1):
        out += str(number)
    # print(out)
    return out
print(func(int(input()) - 1))
# for i in range(1, 51):
    # print("i:{} out:{}".format(i, func(i - 1)))
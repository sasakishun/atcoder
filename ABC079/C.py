s = input()
op = ["+", "-"]


def caliculation(sum, operator, _input):
    if op[operator] == "+":
        sum += _input
    elif op[operator] == "-":
        sum -= _input
    return sum


for i in range(2):
    for j in range(2):
        for k in range(2):
            sum = int(s[0])
            sum = caliculation(sum, i, int(s[1]))
            sum = caliculation(sum, j, int(s[2]))
            sum = caliculation(sum, k, int(s[3]))
            if sum == 7:
                print("{}{}{}{}{}{}{}{}".format(s[0], op[i], s[1], op[j], s[2], op[k], s[3], "=7"))
                exit()
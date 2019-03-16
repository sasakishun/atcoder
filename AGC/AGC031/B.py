n = int(input())
c = [int(input())]
last = [-1 for _ in range(2 * (10 ** 5) + 1)]
for i in range(1, n):
    _c = int(input())
    if _c != c[-1]:  # 連続同数字は1つに連結
        c.append(_c)
# print(c)
out = [0 for _ in range(len(c))]
out[0] = 1
last[c[0]] = 0
for i in range(1, len(c)):
    out[i] = out[i-1]
    if last[c[i]] >= 0:
        # print(out[last[c[i]]])
        out[i] += out[last[c[i]]]
        out[i] %= 10 ** 9 + 7
    last[c[i]] = i
    # print("out:{}".format(out))
    # print("last:{}\n".format(last[:10]))
print(out[-1] % (10 ** 9 + 7))
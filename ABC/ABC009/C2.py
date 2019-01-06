# 入力文字列sを
# k文字まで並び替える場合の辞書順最小
def diff(_s, _t):
    s = sorted(_s)
    t = sorted(_t)
    alphaS = [0 for _ in range(ord("z") - ord("a") + 1)]
    alphaT = [0 for _ in range(ord("z") - ord("a") + 1)]
    count = 0
    for i in range(len(s)):
        # print("s:[{}]:{} s:{}".format(i, s[i], s))
        alphaS[ord(s[i]) - ord("a")] += 1
        alphaT[ord(t[i]) - ord("a")] += 1
    for i in range(len(alphaS)):
        count += abs(alphaS[i] - alphaT[i])
    return count//2


def func(n, k, _s):
    s = [i for i in _s]
    # print("s:{}".format(s))
    remain = [i for i in _s]
    remain.sort()
    out = ""
    for i in range(len(s)):
        # remain.sort()
        # print("\nremain:{}".format(remain))
        for c in range(len(remain)):
            # print("remain:{}".format(remain))
            # remain[c]を「t」に追加する
            # print("cost:{}".format(diff(s[i + 1:], remain[:c] + remain[c + 1:])))
            if s[i] != remain[c] and diff(s[i + 1:], remain[:c] + remain[c + 1:]) <= k - 1:
                # print("1 s[{}]:{} remain[{}]:{} remain:{}".format(i, s[i], c, remain[c], remain[:c] + remain[c+1:]))
                out += remain[c]
                del remain[c]
                k -= 1
                break
            elif s[i] == remain[c] and diff(s[i + 1:], remain[:c] + remain[c + 1:]) <= k:
                # print("2 s[{}]:{} remain[{}]:{} remain:{}".format(i, s[i], c, remain[c], remain[:c] + remain[c+1:]))
                out += remain[c]
                del remain[c]
                break
            """
            else:
                if diff(s[i + 1:], remain[:c] + remain[c + 1:]) <= k:
                    print("not change")
                    out += s[i]
                    break
            """
        # print("k:{} out:{}".format(k, out))
    return out


n, k = [int(i) for i in input().split()]
s = input()
print(func(n, k, s))
"""
print("{}".format(func(2, 3, "abc")) == "abc")
print("{}".format(func(7, 2, "atcoder") == "actoder"))
print("{}".format(func(7, 7, "atcoder") == "acdeort"))
print("{}".format(func(18, 3, "helloworld") == "dehloworll"))
print("{}".format(func(18, 0, "hellbazzfbabforld") == "dehloworll"))
print("{}".format(func(18, 20, "helafdfdfdddzzafb") == "dehloworll"))
print("{}".format(func(18, 1, "rldadfbadf") == "dehloworll"))
"""

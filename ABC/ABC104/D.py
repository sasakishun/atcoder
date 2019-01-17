def func(s):
    alpha = [0, 0, 0]
    ques = 0
    nowQues = 1
    ab = 0  # ABの選び方
    count = 0
    for _s in s:
        if _s == "?":
            count *= 3  # 既にabcとなっている場合の数
            count += ab  # 「? == c」とする場合
            ab *= 3
            # ある?(== B)を末尾とするABの選び方は「A+?」か「?+?」
            if ques > 0:
                ab += alpha[0] * nowQues*3  # (3 ** ques)
            else:
                ab += alpha[0]
            # ？の中からaを選ぶ場合
            if ques > 0:
                ab += ques * nowQues  # (3 ** (ques - 1))
            ques += 1
            if ques > 1:
                nowQues *= 3
        elif _s == "A":
            alpha[0] += 1
        elif _s == "B":
            # あるBを末尾とするABの選び方は「A + B」か「? + B」
            if ques > 0:
                ab += alpha[0] * nowQues*3  # (3 ** ques)
            else:
                ab += alpha[0]
            if ques > 0:
                ab += ques * nowQues  # (3 ** (ques - 1))
            alpha[1] += 1
        elif _s == "C":
            # あるCを末尾とするABCの選び方は「bSelect通り」
            count += ab
            alpha[2] += 1
        count %= 10 ** 9 + 7
        ab %= 10 ** 9 + 7
        nowQues %= 10 ** 9 + 7
        # print("{} -> alpha:{} ab:{} count:{}".format(_s, alpha, ab, count))
    return count % (10 ** 9 + 7)


"""
print(func("A??C") == 8)
print(func("ABCBC") == 3)
print(func("????C?????B??????A???????") == 979596887)
def listToString(_list, split=""):
    maped_list = map(str, _list)  # mapで要素すべてを文字列に
    mojiretu = split.join(maped_list)
    return mojiretu
print(func(listToString(["?" for _ in range(10 ** 5)])))
print("finish")
"""
print(func(input()))

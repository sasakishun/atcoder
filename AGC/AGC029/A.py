_s = input()
s = [_s[i] for i in range(len(_s))]

count = 0
# BB...BW...->WBBBBBB...
# つまり連続している分だけカウントが増える
# そして連続数は変わらない
# WWとなったら連続=0とする
b = 0
# 各wにおいて自分より左にあるBの数だけカウントされる
for i in range(len(s)):
    if s[i] == "B":
        b += 1
    else:
        count += b
print(count)

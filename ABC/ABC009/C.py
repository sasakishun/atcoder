n, k = [int(i) for i in input().split()]
_s = input()
s = []
for i in range(len(_s)):
    s.append([_s[i], i])
s = sorted(s)
out = ["" for _ in range(len(s))]
stack = [False for _ in range(n)]

for i in range(n):
    """
    if stack[i]: #i番目の文字がすでにプッシュされているとき
        for j in range(i, n):
            if stack[s[j][1]]:
                out[i] = s[j]
                stack[s[j][1]] = False
        continue
    """
    if _s[i] != s[i][0]:
        if k == 1:
            # stackの中に_s[i]より小さい値があればそれに入れ替える
            # そうでないならiをインクリメントするだけ
            for j in range(n):
                if stack[s[j][1]]:
                    out[i] = stack[s[j][1]]
                    stack[i] = True
                    stack[s[j][1]] = False
                    continue
            k -= 1
        if stack[s[i][1]] == 1:
            k -= 1
            stack[s[i][1]] = 0
            stack[i] = 1
        elif k >= 2:
            stack[i] = 1

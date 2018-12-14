n = input()
# 1回の処理で、1文字減、連続部分1増
# 最悪でも「len(n)/2」回で終了

# 全ての文字に対し
# それぞれで統一する場合を全部試しても良さそう

score = 1000
left = 0
for i in range(len(n)):
    alpha = n[i] # i文字目で統一する場合を考える
    _left = 0
    left = 0
    for j in range(len(n)):
        if n[j] != alpha:
            _left += 1
        else:
            left = max(left, _left)
            _left = 0
    left = max(left, _left)
    score = min(score, left)
print(score)
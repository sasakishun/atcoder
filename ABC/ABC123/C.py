import math

n = int(input())
a = []
for i in range(5):
    a.append(int(input()))
# a -> b -> c -> d -> e
# 各都市において開始時刻から最終時刻まで見ればいい
# まずa->bにするのに何分かかるか
# 最初と最後だけ分かればいい
prev = 0
lastInput = n
for i in range(len(a)):
    notStop = prev + math.ceil(lastInput / a[i])
    stopped = math.ceil(n / a[i]) + i
    prev = max(notStop, stopped)
    # print("{} vs {}".format(notStop, stopped))
    if notStop < stopped:
        lastInput = n % a[i]
        # print("ok")
    else:
        lastInput %= a[i]
    # print("prev:{} lastInput:{}\n".format(prev, lastInput))
print(prev)
l, x, y, s, d = [int(i) for i in input().split()]

time = 0
# 時計回りに歩くとき
# 速度   = x + y
# 道のり d > s なら d - s
#        s > d なら l - (s - d)
if d > s:
    time = (d - s)/(x + y)
elif d < s:
    time = (l - s + d)/(x + y)
# 反時計回りに歩くとき
# 速度   = - x + y
# 道のり d > s なら l - (d - s)
#        s > d なら s - d
if -x + y > 0:
    if d > s:
        time = min(time, (l - d + s)/(- x + y))
    elif d < s:
        time = min(time, (s - d)/(- x + y))
print(time)

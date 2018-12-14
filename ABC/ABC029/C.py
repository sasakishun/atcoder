x = int(input())
# 要するに6+5+6+5...>=xとなる最小数
count = 0
div = int(x/11)
count += div * 2
if x == div * 11:
    print(count)
elif x <= div * 11 + 6:
    print(count + 1)
else:
    print(count + 2)
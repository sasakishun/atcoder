n, m = [int(i) for i in input().split()]
# n時m分の時
# 短針は(「(60 * (n % 12) + m)」分/720)*360の位置
# 長針は m
print(min(abs((60 * (n % 12) + m)/720 - m/60)*360,
              360-abs((60 * (n % 12) + m) / 720 - m / 60)*360))

n = int(input())
a = [int(i) for i in input().split()]
# 追加する数は常に偶数
# つまり奇数が偶数個あるかというだけの話
binary = 0
nonBinary = 0
for _a in a:
    if _a % 2 == 0:
        binary += 1
    else:
        nonBinary += 1
if nonBinary % 2 == 0:
    print("YES")
else:
    print("NO")
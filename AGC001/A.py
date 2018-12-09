n = int(input())
l = [int(i) for i in input().split()]
l = sorted(l)
# 大きいものは大きいもの同士でペアを組んだ方がよい
# a>b>c>dで, 「b+d>c+d」より証明完了
count = 0
# print(l)
for i in range(n):
    count += l[i*2]
    # print(i)
print("{}".format(count))
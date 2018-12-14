h, w = [int(i) for i in input().split()]

count = 0
# 横に2マス塗る時
count += h * (w - 1)
# 縦に2マス塗る時
count += (h - 1) * w
print(count)
a, b, c = [int(i) for i in input().split()]

# まずbは必ず追加
# a + b + 1枚までcを食べれる
#
print(b + min(c, a + b + 1))
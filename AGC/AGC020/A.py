n, a, b = [int(i) for i in input().split()]

# 勝ち負けが決まるのはAB######か#######ABのようになる時
# 勝負はAとBの距離、そして背後の余白マスのみに依存
# どっちに動こうが関係ない
if (a - b) % 2 == 0:
    print("Alice")
else:
    print("Borys")

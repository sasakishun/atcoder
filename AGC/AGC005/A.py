_x = input()
x = []
for i in _x:
    x.append(i)
count = 0

# 今まで確認してきたものはスタックに入れる
# スタックの頂上がSで次の入力がTならスタックをポップ
stack = []
i = 0
while i < len(x):
    if len(stack) > 0 and stack[-1] == "S" and x[i] == "T":
        del stack[-1]
    else:
        stack.append(x[i])
    i += 1
print(len(stack))
# print(stack)

n = int(input())
a = [int(i) for i in input().split()]
# a : %4 == 0 ->前後に奇数があってもOK
# b : %4 == 2 ->前後も偶数ならOK
# c : %2 == 1 ->前後が4の倍数ならOK
# ex) cacacacac...のように「aの個数」は「cの個数-1」以上になる必要
# 「aの個数」=「cの個数-1」のとき「bの個数」は0つ
# それ以外はcacaca...cabbbbbと出来るのでbはいくつでもよい

table = [0 for i in range(3)]  # [%4==0, %4==2, %2==1]
for i in range(n):
    if a[i] % 4 == 0:
        table[0] += 1
    elif a[i] % 4 == 2:
        table[1] += 1
    else:
        table[2] += 1
if table[0] < table[2] - 1:
    print("No")
elif table[0] == table[2] - 1 and table[1] != 0:
    print("No")
else:
    print("Yes")

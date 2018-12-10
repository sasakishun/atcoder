s = input()

N = [i for i in range(len(s)-1)]  # N = bit探索する桁数
# Nの要素の全組み合わせが出力
sum = 0
for i in range(1 << len(N)):
    output = []
    tmp = s[0]
    for j in range(len(N)):
        if ((i >> j) & 1) == 1:
            tmp += "+" + s[j + 1]
            output.append(j)  # このjが今回探索するindexの1つ
        else:
            tmp += s[j+1]
    # print(output)
    # print(tmp)
    sum += eval(tmp)
print(sum)
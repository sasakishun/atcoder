n, m, l = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

count = 0
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j and j != k and k != i:
                # 縦
                _count = int(n / a[i])
                # 横
                _count *= int(m / a[j])
                # 奥
                _count *= int(l / a[k])
                count = max(count, _count)
print(count)
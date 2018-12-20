def func(n):
    # depthを算出
    _n = n
    depth = 0
    while _n // 2 > 0:
        depth += 1
        _n = _n // 2
    now = 1
    if depth % 2 == 1:
        # このdepthにたどり着くのはTakahashi
        # この層には[2^depth <= n <= 2^(depth) - 1]までの数が含まれる
        # 2^depth <= nに行ければTakahashiの勝ち
        # n < 2^depth に行ければAokiの勝ち、
        # Aokiは左へ移動、Takahashiは右へ移動
        while True:
            #左を目指すTakahashi
            now *= 2
            if now > n:
                return "Aoki"
            #右を目指すAoki
            now *= 2
            now += 1
            if now > n:
                return "Takahashi"
    else:
        while True:
            # 右を目指すTakahashi
            now *= 2
            now += 1
            if now > n:
                return "Aoki"
            # 左を目指すAoki
            now *= 2
            if now > n:
                return "Takahashi"

print(func(int(input())))
"""
print(func(1) == "Aoki")
print(func(5) == "Takahashi")
print(func(7) == "Aoki")
print(func(10) == "Takahashi")
print(func(123456789123456789) == "Aoki")
"""

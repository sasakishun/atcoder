_sx, _sy, _tx, _ty = [int(i) for i in input().split()]
sx, sy, tx, ty = _sx, _sy, _tx, _ty
"""
# 全ての場合を一度tx > sx, ty > syにしてから考える
if sx != tx and sy != ty:
    if tx > sx and ty < sy:
        ty += (ty - sy) * 2
    elif tx < sx and ty > sy:
        tx += (tx - sx) * 2
    elif tx < sx and ty < sy:
        tx += (tx - sx) * 2
        ty += (ty - sy) * 2
elif sx == tx:
    if ty < sy:
        ty += (ty - sy) * 2
else:  # sx==txの形に変換
    if tx < sx:
        tx += (tx - sx) * 2
    sy = sx
    ty = sx
"""
path = ""
# 1回目の行き
for i in range(tx - sx):
    path += "R"
for i in range(ty - sy):
    path += "U"
# 1回目の帰り道
for i in range(tx - sx):
    path += "L"
for i in range(ty - sy):
    path += "D"
# 2回目の行き
path += "D"
for i in range(tx - sx + 1):
    path += "R"
for i in range(ty - sy + 1):
    path += "U"
path += "L"
# 2回目の帰り道
path += "U"
for i in range(tx - sx + 1):
    path += "L"
for i in range(ty - sy + 1):
    path += "D"
path += "R"
"""
else:  # sy == ty
    if tx > sx:
        for i in range(tx - sx):
            path += "U"
        path += "R"
        for i in range(tx - sx):
            path += "D"
        path += "L"
        path += "DRR"
        for i in range(tx - sx + 2):
            path += "U"
        path += "LLDL"
        for i in range(tx - sx):
            path += "D"
        path += "R"
"""
print(path)
"""
if sx != tx and sy != ty:
    if tx > sx:
        for i in range(tx - sx):
            path += "R"
    else:
        for i in range(sx - tx):
            path += "L"
    if ty > sy:
        for i in range(ty - sy):
            path += "U"
    else:
        for i in range(sy - ty):
            path += "D"
    # 帰り道
    if tx > sx:
        for i in range(tx - sx):
            path += "L"
    else:
        for i in range(sx - tx):
            path += "R"
    if ty > sy:
        for i in range(ty - sy):
            path += "D"
    else:
        for i in range(sy - ty):
            path += "U"
    # 2回目の行き
    if tx > sx and ty > sy:
        path += "D"
    elif tx > sx
    if tx > sx:
        for i in range(tx - sx):
            path += "R"
    else:
        for i in range(sx - tx):
            path += "L"
    if ty > sy:
        for i in range(ty - sy):
            path += "U"
    else:
        for i in range(sy - ty):
            path += "D"

elif sx == tx:
    if ty > sy:
        for i in range(ty - sy):
            path += "U"
        path += "R"
        for i in range(ty - sy):
            path += "D"
        path += "L"
    else:
        for i in range(sy - ty):
            path += "D"
        path += "R"
        for i in range(sy - ty):
            path += "U"
        path += "L"
else:  # sy == ty
    if tx > sx:
        for i in range(tx - sx):
            path += "R"
        path += "U"
        for i in range(tx - sx):
            path += "L"
        path += "D"
    else:
        for i in range(sx - tx):
            path += "L"
        path += "U"
        for i in range(sx - tx):
            path += "R"
        path += "D"
print(path)
"""

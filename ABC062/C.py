h, w = [int(i) for i in input().split()]
# h%3=0 or w%3=0なら出力0
# それ以外の場合では
if h % 3 == 0 or w % 3 == 0:
    print(0)
    exit()
minDiff = h * w
for i in range(1, h):
    s1 = w * i
    s2 = int(w / 2) * (h - i)
    s3 = (w - int(w / 2)) * (h - i)
    if s1 > 0 and s2 > 0 and s3 > 0:
        minS = min(s1, min(s2, s3))
        maxS = max(s1, max(s2, s3))
        minDiff = min(minDiff, abs(maxS - minS))
for i in range(1, w):
    s1 = h * i
    s2 = int(h / 2) * (w - i)
    s3 = (h - int(h / 2)) * (w - i)
    if s1 > 0 and s2 > 0 and s3 > 0:
        minS = min(s1, min(s2, s3))
        maxS = max(s1, max(s2, s3))
        minDiff = min(minDiff, abs(maxS - minS))
for i in range(1, h):  # 縦に3分割する場合
    s1 = w * i
    s2 = w * (int((h - i) / 2))
    s3 = w * (h - i - int((h - i) / 2))
    if s1 > 0 and s2 > 0 and s3 > 0:
        minS = min(s1, min(s2, s3))
        maxS = max(s1, max(s2, s3))
        minDiff = min(minDiff, abs(maxS - minS))
for i in range(1, w):  # 横に3分割する場合
    s1 = h * i
    s2 = h * (int((w - i) / 2))
    s3 = h * (w - i - int((w - i) / 2))
    if s1 > 0 and s2 > 0 and s3 > 0:
        minS = min(s1, min(s2, s3))
        maxS = max(s1, max(s2, s3))
        minDiff = min(minDiff, abs(maxS - minS))
print(minDiff)

n = int(input())


# 深さ優先探索で出力
def search(now, lastNum):  # lastNum文字を出力
    if lastNum == 0:
        print(now)
        return
    search(now + "a", lastNum - 1)
    search(now + "b", lastNum - 1)
    search(now + "c", lastNum - 1)
search("", n)
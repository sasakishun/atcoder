import copy

def listToString(_list, split=""):
    maped_list = map(str, _list)  # mapで要素すべてを文字列に
    mojiretu = split.join(maped_list)
    return mojiretu


n = int(input())
cards = [1, 2, 3, 4, 5, 6]
# print(listToString(cards))
# 10**5回操作を実行すると、012345 -> 234501となる
while n > 10**5:
    _cards = copy.deepcopy(cards)    
    _cards[0] = cards[2]
    _cards[1] = cards[3]
    _cards[2] = cards[4]
    _cards[3] = cards[5]
    _cards[4] = cards[0]
    _cards[5] = cards[1]
    cards = copy.deepcopy(_cards)
    n -= (10**5)
for i in range(n):
    # print(i)
    tmp = cards[i % 5]
    cards[i % 5] = cards[i % 5 + 1]
    cards[i % 5 + 1] = tmp
    i += 1
    # print("i:{} cards:{}".format(i, listToString(cards)))
print(listToString(cards))
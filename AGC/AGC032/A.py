def func(b):
    target = [[] for _ in range(len(b) + 1)]
    out = []
    for i in range(len(b)):
        target[b[i]].append(i)
    search = 0
    pos = -1
    while True:
        # print("target:{}".format(target))
        # print("search:{}".format(search))
        # print("pos:{}\n".format(pos))
        for i in range(len(target)):
        if len(target[search]) > 0 and \
                        target[search][-1] > pos:
            out.append(search + 1)
            pos = target[search][-1]
            search += 1
        else:
            search -= 1
            if search == -1:
                return out
            if len(target[search]) > 0:
                target[search].pop()
            if search == 0:
                pos = -1
            else:
                if len(target[search - 1]) == 0:
                    return out
                pos = target[search - 1][-1]

# print(func([0, 1, 0]))
# print(func([1, 1]))
# print(func([0, 0, 0, 1, 1, 0, 1, 2, 1]))

n = int(input())
b = [int(i) - 1 for i in input().split()]
_list = func(b)
if len(_list) == len(b):
    for i in _list:
        print(i)
else:
    print(-1)

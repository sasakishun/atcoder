import queue

n = int(input())
ab = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = [int(i) - 1for i in input().split()]
    ab[a].append(b)
    ab[b].append(a)

stack = [0]
visited = [False for _ in range(n)]
white = 0
black = 0
wQueue = queue.Queue()
wQueue.put(0)
bQueue = queue.Queue()
bQueue.put(n-1)
# print(ab)
while 1:
    wSize = wQueue.qsize()
    if wSize != 0:
        for i in range(wSize):
            now = wQueue.get()
            if not visited[now]:
                white += 1
                visited[now] = True
                for j in range(len(ab[now])):
                        wQueue.put(ab[now][j])
    bSize = bQueue.qsize()
    if bSize != 0:
        for i in range(bSize):
            now = bQueue.get()
            if not visited[now]:
                black += 1
                visited[now] = True
                for j in range(len(ab[now])):
                        bQueue.put(ab[now][j])
    if wSize == 0 and bSize == 0:
        if white > black:
            print("Fennec")
        else:
            print("Snuke")
        # print("w:{} b:{}".format(white, black))
        exit()
n = int(input())
a = [0 for _ in range(n)]
for i in range(n):
    a[i] = int(input()) - 1
visited = [False for _ in range(n)]
visited[0] = True
next = a[0]
count = 1
while True:
    if next == 1:
        print(count)
        exit()
    elif not visited[a[next]]:
        visited[a[next]] = True
        count += 1
        next = a[next]
    else:
        print(-1)
        exit()
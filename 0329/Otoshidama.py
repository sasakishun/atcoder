n, y = map(int, input().split())

flag = 0
for i in reversed(range(n+1)):
    for j in reversed(range(n+1-i)):
        if 10000*i + 5000*j + 1000*(n-i-j) == y:
            print('{} {} {}'.format(i, j, n-i-j))
            flag = 1
            break
    if flag:
        break
    if i == 0:
        print('-1 -1 -1')

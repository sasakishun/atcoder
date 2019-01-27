import queue

n, m = [int(i) for i in input().split()]
a = [0]*(n+m+1)
b = [0]*(n+m+1)
parents = [-1]*n
child = [[] for _ in range(n)]
for i in range(n+m-1):
    a[i], b[i] = [int(i) - 1 for i in input().split()]
    parents[b[i]] = a[i]
    child[a[i]].append(b[i])
root = 0
for i in range(n):
    if parents[i] == -1:
        root = i
        break
_queue = queue.Queue()
for i in child[root]:
    _queue.put([root, i])
parents = [-1 for _ in range(n)]
for k in range(10**10):
    size = _queue.qsize()
    if size == 0:
        break
    for i in range(size):
        _par, _child = _queue.get()
        # print("child:{} par:{}".format(_child, _par))
        parents[_child] = _par
        for j in child[_child]:
            _queue.put([_child, j])
for _par in parents:
    print(_par+1)

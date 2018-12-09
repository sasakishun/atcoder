n, k = [int(i) for i in input().split()]
h = [0 for _ in range(n)]
for i in range(len(h)):
    h[i] = int(input())
h = sorted(h)

_min = h[k-1] - h[0]
for i in range(k, len(h)):
    if h[i] - h[i - k + 1] <= _min:
        _min = h[i] - h[i - k + 1]
print(_min)
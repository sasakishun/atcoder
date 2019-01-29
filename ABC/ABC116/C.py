n = int(input())
h = [int(i) for i in input().split()]
h.append(0)
count = 0
for i in range(1, len(h)):
    if h[i] < h[i-1]:
        count += h[i-1] - h[i]
print(count)
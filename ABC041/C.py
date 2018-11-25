n = int(input())
a = [int(i) for i in input().split()]
out = [[a[i], i+1] for i in range(len(a))]
out = sorted(out)
for i in reversed(range(n)):
    print(out[i][1])
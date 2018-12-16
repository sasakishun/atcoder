n = int(input())
k = int(input())
x = [int(i) for i in input().split()]
_sum = 0
for i in range(len(x)):
    _sum += min(abs(x[i]), abs(x[i] - k)) * 2
print(_sum)
_sum = 0
_maxLoss = 0
for i in range(5):
    a = int(input())
    _maxLoss = max(_maxLoss, (10 - a % 10) % 10)
    _sum += a + (10 - a % 10) % 10
print(_sum - _maxLoss)
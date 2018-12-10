n, a, b = [int(i) for i in input().split()]
sum = 0
for i in range(1, n + 1):
    digitSum = 0
    target = i
    while target > 0:
        digitSum += target % 10
        target = int(target / 10)
    if a <= digitSum <= b:
        sum += i
print(sum)
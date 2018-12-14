n = int(input())

money = 0
for _ in range(n):
    a, b = [int(i) for i in input().split()]
    money += a*b
print(int(money*1.05))
n = int(input())

money = int(n/10)*100
n -= int(n/10)*10
print(money + min(100, n*15))
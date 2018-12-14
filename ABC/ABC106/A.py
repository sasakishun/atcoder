#a = int(input())
#b = int(input())
a, b = [int(i) for i in input().split()]
print(a*b-a-(b-1))
N = int(input())
D,X = map(int, input().split())
sum = 0
for i in range(N):
    sum += int((D-1)/int(input()))+1
print(sum+X)

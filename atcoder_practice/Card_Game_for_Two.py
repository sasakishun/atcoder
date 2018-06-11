N = input()
a = list(map(int, input().split()))
score = list([0, 0])
turn = 0
while len(a) != 0:
    for i in range(len(a)):
        if a[i]==max(a):
            score[turn] += a[i]
            del a[i]
            turn = (turn +1) % 2
            break
print(score[0]-score[1])
        

n = int(input())
s = [i for i in input().split()]

color = [0 for i in range(4)]#P,W,G,Y

for i in range(n):
    if s[i]=="Y":
        print("Four")
        exit()
print("Three")

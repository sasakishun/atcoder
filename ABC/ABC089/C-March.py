n = int(input())
s = [input() for i in range(n)]

name = [0 for i in range(5)]
for i in range(n):
    if s[i][0] == "M":
        name[0] +=1
    elif s[i][0] == "A":
        name[1] +=1
    elif s[i][0] == "R":
        name[2] +=1
    elif s[i][0] == "C":
        name[3] +=1
    elif s[i][0] == "H":
        name[4] +=1
count = 0
for i in range(3):
    for j in range(i+1,4):
        for k in range(j+1,5):
            #print("({},{},{})".format(i,j,k))
            count += name[i]*name[j]*name[k]
print(count)

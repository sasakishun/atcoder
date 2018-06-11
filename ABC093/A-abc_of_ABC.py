s = input()
abc = [0 for i in range(3)]

for i in range(3):
    if s[i]=="a" and abc[0]!=1:
        abc[0]=1
        continue
    elif s[i]=="b" and abc[1]!=1:
        abc[1]=1
        continue
    elif s[i]=="c" and abc[2]!=1:
        abc[2]=1
        continue
    else:
        print("No")
        exit()
print("Yes")

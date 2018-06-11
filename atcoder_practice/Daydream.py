s=list(input())

#print(s)

while len(s)!=0:
    if s[0:5]==list("dream"):
        del s[0:5]
        if len(s)==2:
            if s[0:2]==list("er"):
                del s[0:2]
                continue
        elif len(s)>2:
            if s[0:2]==list("er") and s[2]!="a":
                del s[0:2]
                continue
        continue
    if s[0:6]==list("eraser"):
        del s[0:6]
        continue
    elif s[0:5]==list("erase"):
        del s[0:5]
        continue
    print("NO")
    break
if len(s)==0:
    print("YES")

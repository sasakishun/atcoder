a, b = input().split()

count = 0
for i in range(int(a), int(b)+1):
    flag = 1
    #print(i)
    for j in range(int(len(str(i))/2)):
        #print("{} vs {}".format(str(i)[j], str(i)[-j-1]))
        if str(i)[j]!=str(i)[-j-1]:
            flag = 0
            break
    if flag==1:
        count +=1
print(count)

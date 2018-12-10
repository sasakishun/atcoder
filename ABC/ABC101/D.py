def S(str):
    tmp = 0
    for i in range(len(str)):
        tmp += int(str[i])
    return tmp


k = int(input())

if k < 10:
    for i in range(1, k+1):
        print(i)
    exit()
for i in range(1, 10):
    print(i)
k -= 9
count = 19
while k:
    flag = 0
    for i in range(1000):
        if count * S(str(count + 1 + i)) > (count + 1 + i) * S(str(count)):
            flag = 1
            #if count %100 == 99:
                #print("n:{} m:{}".format(count, count + 1 + i))
    if not flag:
        print(count)
    k -= 1
    count += 10

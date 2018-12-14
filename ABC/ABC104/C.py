d, g = [int(i) for i in input().split()]
p = [[0 for j in range(3)] for i in range(d)]
for i in range(d):
    p[i][1], p[i][2] = [int(i) for i in input().split()]
    p[i][0] = 100*(i+1)
p = sorted(p)
min_num = 10000000
bit = [0 for i in range(d)]
flag = 0
for i in range(2 ** d):
    flag = 0
    sum = 0
    num = 0
    tmp = i
    for j in range(d):
        bit[j] = tmp % 2
        tmp = int(tmp/2)
    for j in range(d):
        if bit[j] == 1:
            num += p[j][1]
            sum += p[j][1]*p[j][0] + p[j][2]
    #print("sum:{} num:{} bit:{}".format(sum,num,bit))
    if sum >= g:
        if num < min_num:
            min_num = num
            #print(num)
            continue
    else:
        res = g - sum
        for j in range(d):
            if bit[j] == 0:
                if res < p[j][0]*p[j][1]:
                    for k in range(p[j][1]-1):
                        #print("sum:{} num:{} bit:{}".format(sum, num, bit))
                        num += 1
                        sum += p[j][0]
                        res -= p[j][0]
                        if res <= 0:
                            if num < min_num:
                                min_num = num
                            break
print(min_num)
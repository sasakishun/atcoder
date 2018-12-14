import math

n = int(input())
ng = [0 for _ in range(3)]
for i in range(3):
    ng[i] = int(input())
for i in range(3):
    if ng[i] == n:
        print("NO")
        exit()
ng = list(reversed(sorted(ng)))
ng.append(-1)
# 1か2か3を引く処理を100回
# 基本的には3を引いていく,
# 3を引くとNG数字にあたる時は2を引く
# それでもだめなら1を引く
ngCount = 0
count = 0
while ngCount < 3:
    # print("n:{} ngCount:{}".format(n, ngCount))
    if n < ng[ngCount]:
        ngCount += 1
        continue
    if (n - ng[ngCount]) % 3 == 0:
        count += int((n - ng[ngCount]) / 3)
        if ngCount > 0 and ng[ngCount - 1] == ng[ngCount] + 1:
            if ngCount > 1 and ng[ngCount - 2] == ng[ngCount - 1] + 1:
                print("NO")
                exit()
            else:
                n = ng[ngCount] + 2
        else:
            n = ng[ngCount] + 1
        continue
        if n - 3 != ng[ngCount+1]:
            n -= 3
            count += 1
        elif n - 2 != ng[ngCount+1]:
            n -= 2
            count += 1
    ngCount += 1
count += int(math.ceil(n/3))
if count <= 100:
    print("YES")
else:
    print("NO")
# print(count)
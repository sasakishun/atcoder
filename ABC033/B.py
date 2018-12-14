from operator import itemgetter

n = int(input())
s = [["", 0] for _ in range(n)]
_sum = 0
for i in range(len(s)):
    s[i] = [i for i in input().split()]
    s[i][1] = int(s[i][1])
    _sum += int(s[i][1])
s.sort(key=itemgetter(1))
if int(s[-1][1]) > _sum/2:
    print(s[-1][0])
else:
    print("atcoder")

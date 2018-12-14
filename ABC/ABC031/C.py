import math

n, m = [int(i) for i in input().split()]
# c:「m-2」とすれば,s:「n+1」と出来る
count = 0
# if int((m-2*n)/4) >= 0:
if m - 2*n > 0:
    count = max(count, min(n + int((m - 2 * n) / 4),
                           int(m / 2 - (m - 2 * n) / 4)))
    # print(count)
    # if math.ceil((m-2*n)/4) >= 0:
    count = max(count, min(n + math.ceil((m - 2 * n) / 4),
                           int(m / 2) - math.ceil((m - 2 * n) / 4)))
    # print(count)
count = max(count, min(n, int(m / 2)))
print(count)

n = int(input())
a, b = [int(i) for i in input().split()]
p = [int(i) for i in input().split()]
p.sort()
one = 0
two = 0
three = 0
for i in range(n):
    if p[i] <= a:
        one += 1
    elif p[i] <= b:
        two += 1
    else:
        three += 1
print(min(one, two, three))
# print("one:{} two:{} three:{}".format(one, two, three))
"""
if one == 0 or two == 0 or three == 0:
    print(0)
else:
    print((one-1)*(two-1)*(three-1))
    """
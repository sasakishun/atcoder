import math

def func(n, a, b, v):
    v.sort()
    v.reverse()
    target = v[a - 1]
    count = 0
    innerCount = 0
    for i in range(n):
        if v[i] == target:
            if i < a:
                innerCount += 1
            count += 1
    # aつすべてがv[i] == targetの場合
    if v[0] == target:
        out = 0
        for i in range(a, min(count, b) + 1):
            out += math.factorial(count) \
                   // (math.factorial(count - i)
                       * math.factorial(i))
        print(sum(v[:a])/a)
        print(out)
    elif v[a-1] == v[a]:
        print(sum(v[:a])/a)
        print(math.factorial(count)
              // (math.factorial(count - innerCount)
                  * math.factorial(innerCount)))
    else:
        print(sum(v[:a])/a)
        print(1)
n, a, b = [int(i) for i in input().split()]
v = [int(i) for i in input().split()]
func(n, a, b, v)
"""
func(5, 2, 2, [5, 4, 3, 2, 1])
print()
func(4, 2, 3, [20, 10, 10, 10])
print()
func(5, 1, 5, [1000000000000000, 999999999999999, 999999999999998, 999999999999997, 999999999999996])
print()
func(50, 1, 50, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
# print("func({}, {}, {}, {})".format(n, a, b, v))
"""

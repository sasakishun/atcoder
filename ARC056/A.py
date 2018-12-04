import math

a, b, k, l = [int(i) for i in input().split()]

print(min(min(a*k, b * math.ceil(k/l)),
          b * int(k/l) + a * (k % l)))
# print(a*k)
# print(b * math.ceil(k/l))
# print(b * int(k/l) + a * (k % l))
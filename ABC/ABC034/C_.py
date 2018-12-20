import math

w, h = [int(i) for i in input().split()]

# 右がW-1つ、上がH-1つの順列の場合の数
# つまり(W + H - 2)!/((W-1)!*(H-1)!)

"""
print((math.factorial(w + h - 2) //
       (math.factorial(w - 1) * math.factorial(h - 1)))
      % (10 ** 9 + 7))
"""
print((math.factorial(w + h - 2)
       * pow(math.factorial(w - 1),
             10 ** 9 + 5,
             10 ** 9 + 7)
       * pow(math.factorial(h - 1),
             10 ** 9 + 5,
             10 ** 9 + 7))
      % (10 ** 9 + 7))

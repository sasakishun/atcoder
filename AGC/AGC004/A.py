a, b, c = [int(i) for i in input().split()]
# a*b*cの直方体を2分割する場合を考えればよい

minDiff = a * b * c
minDiff = min(minDiff, abs(int(a/2)*b*c - (a-int(a/2))*b*c))
minDiff = min(minDiff, abs(int(b/2)*c*a - (b-int(b/2))*c*a))
minDiff = min(minDiff, abs(int(c/2)*a*b - (c-int(c/2))*a*b))
print(minDiff)
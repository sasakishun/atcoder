n = int(input())
if n == 1:
    print(0)
    exit()
_min = n

# O(n)で縦 == iとして全探索
for i in range(1, n):
    _min = min(_min, abs(i - int(n/i)) + n - (i * int(n/i)))
print(_min)
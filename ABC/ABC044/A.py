n = int(input())
k = int(input())
x = int(input())
y = int(input())

print(x * min(n, k) + max(0, y * (n - k)))
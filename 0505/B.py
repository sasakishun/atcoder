a, b, c = [int(i) for i in input().split()]
k = int(input())
max_int = max(a, b, c) * pow(2, k)

print(max_int + (a + b + c - max(a, b, c)))

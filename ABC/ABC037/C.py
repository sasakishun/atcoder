n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
a = [0] + a
for i in range(1, len(a)):
    a[i] += a[i-1]
sum = 0
for i in range(1, n-k+2):
    # print("a[{}]...a[{}] :{}".format(i, i + k - 1, a[i + k - 1] - a[i - 1]))
    sum += a[i + k - 1] - a[i - 1]
print(sum)
# print(a)

n = int(input())
a = [int(i) for i in input().split()]
sum = [0 for i in range(n)]

count = [1 for i in range(n)]
sum[0] = a[0]

r = 1
while r < n:
    if sum[r - 1] ^ a[r] == sum[r - 1] + a[r]:
        count[r] = count[r - 1] + 1
        sum[r] = sum[r - 1] + a[r]
        print("---------ok")
    else:
        sum[r] = a[r]
    r += 1
    print("")

for i in range(n - 1):
    count[i + 1] += count[i]
print(count[-1])

n = int(input())
a = [int(i) for i in input().split()]
#a = sorted(a)

sum = [0 for i in range(n)]
sum[0] = a[0]
for i in range(1, n):
    sum[i] = a[i]+sum[i-1]

pivot = [0 for i in range(3)]
for i in range(n):
    if sum[i] > sum[-1]/2:
        pivot[1] = i
        break

for i in range(pivot[1]):
    if sum[i]-sum[0] > (sum[pivot[1]-1]-sum[0])/2:
        pivot[0] = i
        break
for i in range(pivot[1], n):
    if sum[i]-sum[pivot[1]-1] > (sum[-1]-sum[pivot[1]-1])/2:
        pivot[2] = i+1
        break
local = [0 for i in range(4)]
for i in range(pivot[0]):
    local[0] += a[i]
for i in range(pivot[0], pivot[1]):
    local[1] += a[i]
for i in range(pivot[1], pivot[2]):
    local[2] += a[i]
for i in range(pivot[2], n):
    local[3] += a[i]
print(sum)
print(pivot)
print(local)
print(abs(max(local)-min(local)))
n = int(input())
count = 0
if n % 2 == 0:
    for i in range(1, int(n/2)):
        count += i*2
    print(count*2)
else:
    for i in range(1, int(n/2)):
        count += 2*i - 1
    count *= 2
    count += n - 2
    print(count)
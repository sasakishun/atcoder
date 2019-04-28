a, b, k = [int(i) for i in input().split()]

for i in reversed(range(max(a, b)+1)):
    if a % i == 0 and b % i == 0:
        k -= 1
        if k == 0:
            print(i)
            exit()
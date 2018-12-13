n = int(input())
a = [int(i) for i in input().split()]

# a[i]%2==1 and a%3==(1or0)ならOK
# つまりa[i] % 6 == (1,3)
out = [0 for _ in range(len(a))]
for i in range(len(a)):
    if a[i] % 6 == 0:
        out[i] = 3
    elif a[i] % 6 == 2:
        out[i] = 1
    elif a[i] % 6 == 4:
        out[i] = 1
    elif a[i] % 6 == 5:
        out[i] = 2
    else:
        out[i] = 0
print(sum(out))
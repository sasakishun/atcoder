a, b, k = [int(i) for i in input().split()]

counter = 0
for i in range(k):
    if a % 2 == 1:
        a -= 1
    b += int(a/2)
    a = int(a/2)
    counter += 1
    if counter >= k:
        print("{} {}".format(a, b))
        exit()

    if b % 2 == 1:
        b -= 1
    a += int(b/2)
    b = int(b/2)
    counter += 1
    if counter >= k:
        print("{} {}".format(a, b))
        exit()
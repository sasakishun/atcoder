n = input()
_sum = sum([int(n[i]) for i in range(len(n))])
if int(n) % _sum == 0:
    print("Yes")
else:
    print("No")
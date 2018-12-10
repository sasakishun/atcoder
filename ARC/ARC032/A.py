def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 2
    return True


n = int(input())
_sum = 0
for i in range(1, n+1):
    _sum += i
if is_prime(_sum):
    print("WANWAN")
else:
    print("BOWWOW")
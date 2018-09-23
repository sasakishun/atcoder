def is_prime(q):
    q = abs(q)
    if q == 2:
        return True
    if q < 2 or q & 1 == 0:
        return False
    return pow(2, q - 1, q) == 1

prime_list = [int(i) for i in range(10000) if is_prime(i)]

n = int(input())

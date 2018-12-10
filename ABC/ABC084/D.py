class imosOneDimension:
    def __init__(self, size):
        self.table = [0 for i in range(size)]

    def setTable(self):
        for i in range(len(self.table) - 1):
            if self.is_prime(i) and self.is_prime(int((i + 1) / 2)):
                self.table[i] = 1
                # self.table[i] += self.table[i - 1]

    def cumulativeSum(self):
        for i in range(1, len(self.table)):
            self.table[i] += self.table[i - 1]

    def is_prime(self, n):
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


imos = imosOneDimension(size=10 ** 5 + 1)
imos.setTable()
imos.cumulativeSum()
q = int(input())
for i in range(q):
    l, r = [int(i) for i in input().split()]
    print(imos.table[r] - imos.table[l - 1])

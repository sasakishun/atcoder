n, q = [int(i) for i in input().split()]
s = input()
imos = [0 for _ in range(len(s))]
for i in range(1, len(s)):
    if s[i] == "C" and s[i-1] == "A":
        imos[i] = 1
for i in range(1, len(s)):
    imos[i] += imos[i-1]
for _ in range(q):
    l, r = [int(i) - 1 for i in input().split()]
    print(imos[r] - imos[l])
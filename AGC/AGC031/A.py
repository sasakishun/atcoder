n = int(input())
s = input()
alpha = [0 for _ in range(ord("z") - ord("a") + 1)]

for i in range(len(s)):
    alpha[ord(s[i]) - ord("a")] += 1
# print(alpha)
_sum = alpha[0] + 1
for i in range(1, len(alpha)):
    _sum *= alpha[i] + 1
print((_sum - 1) % (10 ** 9 + 7))

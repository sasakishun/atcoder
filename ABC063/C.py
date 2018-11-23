n = int(input())
s = [0 for i in range(n)]
counter = 0
for i in range(n):
    s[i] = int(input())
    counter += s[i]
# 全探査だとO(2^100)となり不適
# 全問正解した場合から,
# 得点が10の倍数でない1問を取り除く
s = sorted(s)
if counter % 10 != 0:
    print(counter)
    exit()
else:
    for i in range(n):
        if (counter - s[i]) % 10 != 0:
            print(counter - s[i])
            exit()
print(0)
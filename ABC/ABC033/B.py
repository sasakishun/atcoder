s = input()
k = int(input())

# 重複がない部分文字列の数
# まず部分文字列を列挙
out = []
for i in range(len(s) - k + 1):
    out.append(s[i:i+k])
out.sort()
out.append("sentinel")
count = 0
for i in range(1, len(out)):
    if out[i] != out[i-1]:
        count += 1
print(count)
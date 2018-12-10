n = int(input())
a = [int(i) for i in input().split()]

# 単調非減少か単調非増加
# 単調非減少 = 上昇 or 0
# 単調非増加 = 減少 or 0

up = False
down = False
count = 0
i = 1
while i < len(a):
    # print("\nup:{} down:{}".format(up, down))
    if a[i] - a[i - 1] > 0 and down:
        # print("+counted a[{}]:{} a[{}]:{}".format(i, a[i], i-1, a[i-1]))
        up = False
        down = False
        count += 1
    elif a[i] - a[i - 1] < 0 and up:
        # print("-counted a[{}]:{} a[{}]:{}".format(i, a[i], i - 1, a[i - 1]))
        up = False
        down = False
        count += 1
    elif a[i] - a[i-1] > 0:
        up = True
    elif a[i] - a[i-1] < 0:
        down = True
    i += 1
print(count + 1)

n = int(input())
w = [i for i in input().split()]

count = 0
for i in range(len(w) - 1):
    if w[i] == "TAKAHASHIKUN" or w[i] == "Takahashikun" or w[i] == "takahashikun":
        count += 1
if w[-1] == "TAKAHASHIKUN." or w[-1] == "Takahashikun." or w[-1] == "takahashikun.":
    count += 1
print(count)

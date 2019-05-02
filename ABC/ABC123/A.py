a = []
for i in range(5):
    a.append(int(input()))
k = int(input())
a.sort()
if a[-1] - a[0] > k:
    print(":(")
else:
    print("Yay!")
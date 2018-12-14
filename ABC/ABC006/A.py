n = int(input())
if n % 3 == 0:
    print("YES")
    exit()
for i in range(len(str(n))):
    if str(n)[i] == "3":
        print("YES")
        exit()
print("NO")
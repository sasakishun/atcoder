n = int(input())
count = 0
for i in range(1, n+1):
    div_count = 0
    for j in range(1, i+1):
        if i % j == 0 and j % 2 == 1:
            div_count += 1
    if div_count == 8:
        count += 1

print(count)

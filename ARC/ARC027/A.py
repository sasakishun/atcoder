h, m = [int(i) for i in input().split()]
time = 0
if m > 0:
    time += 60 - m
    h += 1
if h < 18:
    time += 60*(18-h)
print(time)
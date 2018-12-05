s = input()

diff = 1000
for i in range(len(s) - 2):
    diff = min(diff, abs(753 - int(s[i:i+3])))
print(diff)
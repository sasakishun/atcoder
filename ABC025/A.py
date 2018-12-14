_s = input()
n = int(input()) - 1
s = [_s[i] for i in range(len(_s))]
s.sort()

# 8番目とは
# 12345,12354,12435,12453,13245,13254,13425,13452
print("{}{}".format(s[int(n/5)], s[n%5]))
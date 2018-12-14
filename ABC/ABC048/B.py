a, b, x = [int(i) for i in input().split()]
divableA = (a-1) // x
divableB = b // x
print(divableB - divableA)

n = int(input())

i = 0
while True:
    if n <= int((i*(i+1))/2):
        print(i)
        exit()
    else:
        i += 1
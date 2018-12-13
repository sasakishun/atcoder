

def func(m):
    if m < 100:
        return "00"
    elif m <= 5000:
        if m < 1000:
            return "0{}".format(int((m/1000)*10))
        else:
            return int((m/1000)*10)
    elif 6000 <= m <= 30000:
        return int((m/1000)) + 50
    elif 35000 <= m <= 70000:
        return int(((m/1000) - 30)/5) + 80
    elif 70000 < m:
        return 89
#for i in range(702):
    #print("i:{} func:{}".format(i*100, func(i*100)))
m = int(input())
print(func(m))
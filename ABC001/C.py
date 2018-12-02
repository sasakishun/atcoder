deg, dis = [int(i) for i in input().split()]
deg /= 10
min = 11.25
max = 33.75
find = False
for i in range(16):
    if min < deg < max:
        if i == 0:
            deg = "NNE"
            find = True
        if i == 1:
            deg = "NE"
            find = True
        if i == 2:
            deg = "ENE"
            find = True
        if i == 3:
            deg = "E"
            find = True
        if i == 4:
            deg = "ESE"
            find = True
        if i == 5:
            deg = "SE"
            find = True
        if i == 6:
            deg = "SSE"
            find = True
        if i == 7:
            deg = "S"
            find = True
        if i == 8:
            deg = "SSW"
            find = True
        if i == 9:
            deg = "SW"
            find = True
        if i == 10:
            deg = "WSW"
            find = True
        if i == 11:
            deg = "W"
            find = True
        if i == 12:
            deg = "WNW"
            find = True
        if i == 13:
            deg = "NW"
            find = True
        if i == 14:
            deg = "NNW"
            find = True
        break
    min += 22.5
    max += 22.5
if not find:
    deg = "N"
if 0.0 <= round(dis / 60, -1) <= 0.2:
    dis = "0"
elif 0.3 <= round(dis / 60, -1) <= 1.5:
    dis = "1"
elif 1.6 <= round(dis / 60, -1) <= 3.3:
    dis = "2"
elif 3.4 <= round(dis / 60, -1) <= 5.4:
    dis = "3"
elif 5.5 <= round(dis / 60, -1) <= 7.9:
    dis = "4"
elif 8 <= round(dis / 60, -1) <= 10.7:
    dis = "5"
elif 10.8 <= round(dis / 60, -1) <= 13.8:
    dis = "6"
elif 13.9 <= round(dis / 60, -1) <= 17.1:
    dis = "7"
elif 17.2 <= round(dis / 60, -1) <= 20.7:
    dis = "8"
elif 20.8 <= round(dis / 60, -1) <= 24.4:
    dis = "9"
elif 24.5 <= round(dis / 60, -1) <= 28.4:
    dis = "10"
elif 28.5 <= round(dis / 60, -1) <= 32.6:
    dis = "11"
elif 32.7 <= round(dis / 60, -1):
    dis = "12"
if dis == "0":
    print("{} {}".format("C", 0))
else:
    print("{} {}".format(deg, dis))
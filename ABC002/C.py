xa, ya, xb, yb, xc, yc = [int(i) for i in input().split()]
print(0.5 * abs((xa-xc)*(yb-yc)-(xb-xc)*(ya-yc)))
def func(k, a, b):
    if b > a + 2 and k >= a - 1:
            print(a + (b - a) * ((k - a + 1) // 2)
                  + (k - a + 1) % 2)
    else:
        print(1 + k)
#func(4, 2, 6)
#func(7, 3, 4)
#func(314159265, 35897932, 384626433)
k, a, b = [int(i) for i in input().split()]
func(k, a, b)

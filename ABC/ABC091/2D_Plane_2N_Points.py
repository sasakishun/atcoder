def sort_x(a):
    min = 100000
    min_num = 0
    n = len(a)
    A=[[0, 0] for i in range(n)]
    left_list = [1 for i in range(n)]

    for j in range(n):
        for i in range(n):
            if left_list[i]==1 and int(a[i][0]) < min:
                min = int(a[i][0])
                min_num = i
        left_list[min_num] = 0
        A[j] = a[min_num]
        min=100000
    return A

def sort_y(a):
    min = 100000
    min_num = 0
    n = len(a)
    A=[[0, 0] for i in range(n)]
    left_list = [1 for i in range(n)]

    for j in range(n):
        for i in range(n):
            if left_list[i]==1 and int(a[i][1]) < min:
                min = int(a[i][1])
                min_num = i
        left_list[min_num] = 0
        A[j] = a[min_num]
        min=100000
    return A

if __name__ == '__main__':
    n = int(input())
    a_ = [input().split() for i in range(n)]
    c_ = [input().split() for i in range(n)]
    a = [[0,0] for i in range(n)]
    c = [[0,0] for i in range(n)]
    c = sort_x(c_)
    a = sort_y(a_)
    
    frend_num = 0
    #print(a)
    #print(c)
    #min = 100000
    #min_index = 0
    filter_a = [1 for i in range(n)]
    for j in range(n):
        for i in reversed(range(n)):
            if filter_a[i]==1 and int(a[i][0])<int(c[j][0]) and int(a[i][1])<int(c[j][1]):
                        filter_a[i]=0
                        frend_num += 1
                        #print("{},{}".format(a,c))
                        #print("{}".format(filter_a))
                        #print("friend is detected")
                        break
    print(frend_num)

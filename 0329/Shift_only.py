N=int(input())
A=list(map(int, input().split()))
# print(A)
max_div_num=100
for i in range(N):
    for j in range(100):
        if A[i] % 2 == 0:
            A[i] /= 2
        else:
            if j < max_div_num:
                max_div_num = j
            break
print(max_div_num)        

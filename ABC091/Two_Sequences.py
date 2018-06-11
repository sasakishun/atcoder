def multi(x, n):
    X = 1
    for i in range(n):
        X *=x
    return X

def binary(x):
    digit = 0
    x = int(x)
    while 1:
        if x/multi(2, digit+1) >= 1:
            digit +=1
        else:
            break
    digit += 1
    bin = [0 for i in range(28)]
    
    for i in reversed(range(digit)):
        if x/multi(2, i)>=1:
            bin[-i-1] = 1
            x -= multi(2,i)
    return bin

def binary_to_ten(x):
    sum = 0
    for i in range(len(x)):
        if x[-i-1]==1:
            sum+=multi(2,i)
    return sum
def culicurate_xor(x):
    for i in range(28):
        if int(x[i]) != 1:
            x[i] = 0
    return x

if __name__ == '__main__':
    n = int(input())
    a = input().split()
    b = input().split()
    array = [[0 for i in range(n)] for j in range(n)]
    
    for i in range(n):
        for j in range(n):
            array[i][j] = binary(int(a[i])+int(b[j]))
    xor = [0 for i in range(28)]
    
    for i in range(n):
        for j in range(n):
            for k in range(28):
                xor[k] = (xor[k]+int(array[i][j][k]))%2
    
    for k in range(28):
        if int(xor[k])%2==0:
            xor[k]=0
        else:
            xor[k]==1
    print(binary_to_ten(xor))
                         
                              
                        
    
    

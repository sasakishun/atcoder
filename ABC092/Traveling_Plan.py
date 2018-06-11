if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    A = list([0])
    A.extend(a)
    A.append(0)

    sum = 0
    for i in range(1, n+2):
        sum += abs(A[i]-A[i-1])
    for i in range(1, n+1):
        print(sum-abs(A[i]-A[i-1])-abs(A[i+1]-A[i])+abs(A[i+1]-A[i-1]))

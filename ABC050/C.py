n = int(input())
a = [int(i) for i in input().split()]
# aで嘘がある場合は出力0
# aは,nが奇数なら[0, 2, 2, 4, 4, 6, 6, ...]
# aは,nが偶数なら[1, 1, 3, 3, 5, 5, 7, ...]
valid = [i + (i+n+1) % 2 for i in range(n)]
a = sorted(a)
if a != valid:
    print(0)
else:
    # aが正しいなら答えはaに関係なくnのみで決まる
    # n==5->2**2, n==6->2**3, n==7->2**3, n==8->2**4
    # つまり答えは2**(int(n/2))
    out = 1
    for i in range(int(n/2)):
        out *= 2
        out %= 10**9+7
    print(out)
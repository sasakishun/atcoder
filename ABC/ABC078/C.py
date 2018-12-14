n, m = [int(i) for i in input().split()]
# n-mケースでは100ms
# mケースでは1900msで確率1/2
# つまり(100*(n-m)+1900*m)*(2**m)
print((100*(n-m)+1900*m)*(2**m))
def toSmall(c):
    _c = ord(c)
    if _c <= ord("Z"):
        _c += ord("a") - ord("A")
    return chr(_c)

def toLarge(c):
    _c = ord(c)
    if _c >= ord("a"):
        _c -= ord("a") - ord("A")
    return chr(_c)

s = input()
out = toLarge(s[0])
for _s in s[1:]:
    out += toSmall(_s)
print(out)
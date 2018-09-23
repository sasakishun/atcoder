s = input()
alpha = [0 for i in range(26)]
number = ""
number_int = 1

i = 0
while i < len(s):
    while ord("0") <= ord(s[i]) <= ord("9"):
        number += s[i]
        i += 1
    if number != "":
        number_int = int(number)
        number = ""
    else:
        number_int = 1
    if s[i] == "(":
        i += 1
        while s[i] != ")":
            alpha[ord(s[i]) - ord("a")] += number_int
            i += 1
    else:
        alpha[ord(s[i])-ord("a")] += number_int
    i += 1
for i in range(len(alpha)):
    print("{} {}".format(chr(i+ord("a")), alpha[i]))

#abcdefg10h12(ij2(3k))l9mnop4(3(2(6(qq)r)s5tu)7v5w)x15(yz)
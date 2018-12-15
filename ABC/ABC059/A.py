s = [i for i in input().split()]
print("{}{}{}".format(
    chr(ord(s[0][0]) + ord("A") - ord("a")),
    chr(ord(s[1][0]) + ord("A") - ord("a")),
    chr(ord(s[2][0]) + ord("A") - ord("a"))))
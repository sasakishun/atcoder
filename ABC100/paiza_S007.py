s = input()
alpha = [0 for i in range(26)]
number = ""
number_int = 1
number_list = []

for i in range(len(s)):
    #print("{}:{}:{}:{}".format(s[i], number,number_int, number_list))
    if ord("0") <= ord(s[i]) <= ord("9"):
        number += str(s[i])
    elif s[i] == "(":
        number_int *= int(number)
        number_list.append(int(number))
        number = ""
    elif s[i] == ")":
        number_int = int(number_int/int(number_list[-1]))
        del number_list[-1]
    elif i > 0 and ord("0") <= ord(s[i-1]) <= ord("9"):
        alpha[ord(s[i]) - ord("a")] += number_int*int(number)
        number = ""
    else:
        alpha[ord(s[i]) - ord("a")] += number_int

for i in range(len(alpha)):
    print("{} {}".format(chr(i+ord("a")), alpha[i]))

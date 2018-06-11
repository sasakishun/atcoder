if __name__ == '__main__':
    s = input()
    alpha = list([1 for i in range(26)])
    if len(s) != 26:
        for i in range(len(s)):
            if(alpha[ord(s[i])-97] == 0):
                print("-1")
                exit()
            alpha[ord(s[i])-97] = 0
        for i in range(len(alpha)):
            if alpha[i]==1:
                print(str(s)+chr(i+97))
                exit()
        print("-1")
        exit()
    else:
        max = ord(s[-1])-97
        alpha[ord(s[-1])-97] = 0
        
        for i in reversed(range(len(s)-1)):
            if ord(s[i])-97 <  max:
                for j in range(len(alpha)):
                    if alpha[j] == 0 and ord(s[i])-97<j:
                        print(s[:i]+chr(j+97))
                        exit()
            else:
                max = ord(s[i])-97
            alpha[ord(s[i])-97] = 0
        print("-1")
        exit()

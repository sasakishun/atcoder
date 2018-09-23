s = input()
t = input()
alpha = [i for i in range(ord("z")-ord("a")+1)]
visited = [0 for i in range(ord("z")-ord("a")+1)]

for i in range(len(s)):
    if alpha[ord(s[i])-ord("a")] != ord(t[i])-ord("a"):
        if visited[ord(t[i]) - ord("a")] == 1:
            print("No")
            exit()
        else:
            tmp = alpha[ord(s[i]) - ord("a")]
            for j in range(len(alpha)):
                if alpha[j] == tmp:
                    alpha[j] = ord(t[i]) - ord("a")
                elif alpha[j] == ord(t[i]) - ord("a"):
                    alpha[j] = tmp
    visited[ord(t[i]) - ord("a")] = 1
print("Yes")

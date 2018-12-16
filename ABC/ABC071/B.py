s = input()
alpha = [True for _ in range(26)]
for _s in s:
    alpha[ord(_s) - ord("a")] = False
for i in range(len(alpha)):
    if alpha[i]:
        print(chr(i + ord("a")))
        exit()
print("None")
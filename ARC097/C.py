s = input()
k = int(input())

sub = ["zzzzz" for i in range(k)]


def compare(sub_word):
    for i in range(len(sub)):
        #print("{} vs {}".format(sub[i], sub_word))
        if sub_word == sub[i]:
            return
        if sub_word < sub[i]:
            #print("----")
            for j in reversed(range(i, k - 1)):
                sub[j + 1] = sub[j]
            sub[i] = sub_word
            return


count = 0
for i in range(len(s)):
    for j in range(i, min(i + k, len(s))):
        compare(s[i:j + 1])
print(sub[-1])

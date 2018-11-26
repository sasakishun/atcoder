s = input()

si = "WBWBWWBWBWBWWBWBWWBWBWBW"
onpu = ["Do", "Do", "Re", "Re", "Mi", "Fa", "Fa", "So", "So", "La", "La", "Si"]
# 12文字同じなら一意に確定
for i in range(12):
    if s[:12] == si[i:i + 12]:
        print(onpu[i])

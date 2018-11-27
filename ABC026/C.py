class Tree:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        # self.childExist = [False for i in range(n)]
        self.money = [0 for i in range(n)]  # [0]が子最大値、[1]が子最小値

    def show(self):
        for i in range(n):
            print("node:{} par:{} money:{}".format(i, self.par[i], self.money[i]))

    def search(self, node):
        findFlag = False
        maxSalary = 0
        minSalary = 0
        for i in range(n):
            # print("node:{} i:{}".format(node, i))
            if self.par[i] == node:
                # print("node:{} par:{}".format(node, self.par[i]))
                if not findFlag:
                    maxSalary = self.search(i)
                    minSalary = maxSalary
                else:
                    childSalary = self.search(i)
                    maxSalary = max(maxSalary, childSalary)
                    minSalary = min(minSalary, childSalary)
                findFlag = True
        if findFlag:
            self.money[node] = maxSalary + minSalary + 1
        if not findFlag:
            self.money[node] = 1
        return self.money[node]


n = int(input())
tree = Tree(n)
b = [0 for i in range(n)]
for i in range(1, n):
    b[i] = int(input()) - 1
# b = sorted(b)
tree.par[0] = -1
for i in range(1, n):
    tree.par[i] = b[i]  # iの親はb[i]
    # tree.childExist[b[i]] = True
# tree.show()
# 葉から順に処理
# for i in reversed(range(1, n)):
    # tree.money[tree.par[i]][0] = max(tree.money[tree.par[i]][0], tree.money[i][0] + tree.money[i][0] + 1)
    # tree.money[tree.par[i]][1] = min(tree.money[tree.par[i]][1], tree.money[i][0] + tree.money[i][0] + 1)
tree.search(0)
# print()
# tree.show()
print(tree.money[0])
# 自分より数字が小さい中で、最も数字が大きいb[i]が上司
# 上司関係の木を構築
# parents = 0
"""
for i in range(1, n):
    tree.par[i] = parents
    if i < n and b[i] != b[i+1]:
        parents = i
"""

n = int(input())
p = [0 for i in range(n)]
for i in range(n):
    p[i] = int(input())

visited = [0 for i in range(n+1)]

for i in range(n):
    visited[p[i]] = visited[p[i] - 1] + 1
print(n - max(visited))

"""
for i in reversed(range(n)):
    if visited[i] == 0:
        visited[i] = 1
        count = 1
        target = p[i] - 1

        for j in reversed(range(i)):
            if p[j] == target:
                count += 1
                visited[j] = count
                target -= 1
"""

import sys
from collections import deque

input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


n, m, v = map(int, input().split())

li = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    li[a].append(b)
    li[b].append(a)

for i in range(len(li)):
    li[i].sort()

visited = [False] * (n + 1)
dfs(li, v, visited)
print()
visited = [False] * (n + 1)
bfs(li, v, visited)

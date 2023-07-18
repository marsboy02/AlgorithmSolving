from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = visited[v] + 1
                queue.append(i)


n = int(input())
first, second = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)
bfs(graph, first, visited)

print(visited[second] if visited[second] > 0 else -1)

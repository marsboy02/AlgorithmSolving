from collections import deque

def bfs(v):
    queue = deque([v])
    visited[v] = 1
    while queue:
        v = queue.popleft()
        if v == g:
            return dist[v]
        for nv in (v+u, v-d):
            if 1 <= nv <= f and not visited[nv]:
                visited[nv] = 1
                queue.append(nv)
                dist[nv] = dist[v] + 1
    if dist[g] == 0:
        return 'use the stairs'

f,s,g,u,d = map(int, input().split())
visited = [0] * (f+1)
dist = [0] * (f+1)
print(bfs(s))
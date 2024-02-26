from collections import deque

def bfs(n):
    queue = deque([n])
    while queue:
        x = queue.popleft()
        if x == k:
            return dist[x]
        for nx in (x-1 , x+1, x*2):
            if 0 <= nx < MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                queue.append(nx)

MAX = 100001
dist = [0] * (MAX + 1)
n, k = map(int,input().split())

print(bfs(n))

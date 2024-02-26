import sys
from collections import deque, defaultdict
input = sys.stdin.readline

dr = [0,0,-1,1]
dc = [-1,1,0,0]

def bfs():
    result = 1
    queue = deque([(0,0)])
    while queue:
        r, c = queue.popleft()
        for tr, tc in turn[(r,c)]:
            if not lights[tr][tc]:
                lights[tr][tc] = 1
                result += 1
                for i in range(4):
                    nr, nc = tr+dr[i], tc+dc[i]
                    if 0 <= nr < n and 0 <= nc < n and visited[nr][nc]:
                        queue.append((nr,nc))
        
        for j in range(4):
            nr,nc = r+dr[j], c+dc[j]
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc] and lights[nr][nc]:
                    queue.append((nr,nc))
                    visited[nr][nc] = 1
    return result

n, m = map(int, input().split())
turn = defaultdict(list)
visited = [[0] * n for _ in range(n)]
visited[0][0] = 1
lights = [[0] * n for _ in range(n)]
lights[0][0] = 1

for _ in range(m):
    sr, sc, tr, tc = map(int, input().split())
    turn[(sr-1,sc-1)].append((tr-1, tc-1))

print(bfs())
import sys
from collections import deque
input = sys.stdin.readline

dr = [0,0,-1,1]
dc = [-1,1,0,0]

def bfs(r,c,i,visited):
    visited[r][c] = True
    queue = deque()
    queue.append((r,c))

    while queue:
        r,c = queue.popleft()
        for j in range(4):
            nr,nc = r+dr[j], c+dc[j]
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] > i and not visited[nr][nc]:
                queue.append((nr,nc))
                visited[nr][nc] = True


n = int(input())
board = []
for _ in range(n):
    temp = list(map(int,input().split()))
    max_height = max(temp)
    board.append(temp)
    
answer = 0
for i in range(max_height):
    visited = [[False] * n for _ in range(n)]
    section = 0
    for r in range(n):
        for c in range(n):
            if board[r][c] > i and not visited[r][c]:
                bfs(r,c,i,visited)
                section += 1
    answer = max(answer, section)
print(answer)


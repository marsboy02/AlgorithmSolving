import sys
from collections import deque
sys.setrecursionlimit(10**6)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = sys.maxsize

dr = [0,0,-1,1]
dc = [-1,1,0,0]

def dfs(r,c):
    global cnt
    if r < 0 or r >= n or c < 0 or c >= n:
        return False
    if board[r][c] == 1:
        board[r][c] = cnt
        for i in range(4):
            nr,nc = r+dr[i], c+dc[i]
            dfs(nr,nc)
        return True

def bfs(k):
    global answer
    visited = [[-1] * n for _ in range(n)]
    queue = deque()
    
    for r in range(n):
        for c in range(n):
            if board[r][c] == k:
                queue.append((r,c))
                visited[r][c] = 0

    while queue:
        r,c = queue.popleft()
        for i in range(4):
            nr,nc = r+dr[i], c+dc[i]
            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue
            if board[nr][nc] > 0 and board[nr][nc] != k:
                answer = min(answer, visited[r][c])
                return
            if board[nr][nc] == 0 and visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c] + 1
                queue.append((nr,nc))

cnt = 2
for r in range(n):
    for c in range(n):
        if dfs(r,c) == True:
            cnt += 1
            
for i in range(2, cnt):
    bfs(i)

print(answer)

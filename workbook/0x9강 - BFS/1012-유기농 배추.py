from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

dr = [0,0,-1,1]
dc = [-1,1,0,0]

def bfs(r,c):
    queue = deque()
    queue.append([r,c])
    board[r][c] = 0
    while queue:
        r,c = queue.popleft()
        for i in range(4):
            nr,nc = r+dr[i], c+dc[i]
            if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 1:
                board[nr][nc] = 0
                queue.append([nr,nc])


for _ in range(t):
    m,n,c = map(int, input().split())
    board = [[0] * n for _ in range(m)]
    for _ in range(c):
        r,c = map(int,input().split())
        board[r][c] = 1
    
    cnt = 0
    for r in range(m):
        for c in range(n):
            if board[r][c] == 1:
                cnt += 1
                bfs(r,c)
    print(cnt)
    
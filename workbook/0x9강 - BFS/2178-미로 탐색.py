from collections import deque

n,m = map(int, input().split())
board = [list(map(int,input())) for _ in range(n)]

dr = [0,0,-1,1]
dc = [-1,1,0,0]

def bfs(r,c):
    queue = deque()
    queue.append([r,c])
    while queue:
        r,c = queue.popleft()
        for i in range(4):
            nr,nc = r+dr[i],c+dc[i]
            if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 1:
                queue.append([nr,nc])
                board[nr][nc] = board[r][c] + 1

    return board[n-1][m-1]

print(bfs(0,0))

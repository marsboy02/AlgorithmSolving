from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dr = [0,0,-1,1]
dc = [-1,1,0,0]

queue = deque()

def bfs():
    cnt = -1
    while queue:
        cnt += 1
        r,c = queue.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 0:
                board[nr][nc] = 1
                queue.append([nr,nc])
    return cnt


for r in range(n):
    for c in range(m):
        if board[r][c] == 1:
            queue.append([r,c])

print(queue)
print(bfs())
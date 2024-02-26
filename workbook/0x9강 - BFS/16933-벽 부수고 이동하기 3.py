from collections import deque
import sys
input = sys.stdin.readline


dr = [0,0,-1,1]
dc = [-1,1,0,0]

n,m,k = map(int, input().split())
MAX = float('inf')

board = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[MAX]*(k+1) for _ in range(m)] for _ in range(n)]
visited[0][0][k] = 0
queue = deque([(0,0,1,k)])
result = MAX

while queue:
    r, c, t, left = queue.popleft()
    if (r,c) == (n-1, m-1):
        result = min(result, t)
        continue

    daytime = t % 2
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            if board[nr][nc] == 0 and visited[nr][nc][left] > t:
                visited[nr][nc][left] = t
                queue.append([nr,nc,t+1,left])
            if board[nr][nc] == 1 and left and visited[nr][nc][left-1] > t:
                if daytime:
                    visited[nr][nc][left-1] = t
                    queue.append([nr, nc, t+1, left-1])
                else:
                    queue.append([r,c,t+1,left])

print(result if result < MAX else -1)
        
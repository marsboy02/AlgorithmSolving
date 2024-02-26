from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

dr = [0,0,-1,1]
dc = [-1,1,0,0]

def bfs(r,c,z):
    queue = deque()
    queue.append([r,c,z])
    while queue:
        r,c,z = queue.popleft()
        if r == n-1 and c == m-1:
            return visited[r][c][z]
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if board[nr][nc] == 1 and z == 0:
                    visited[nr][nc][1] = visited[r][c][0] + 1
                    queue.append([nr,nc,1])
                elif board[nr][nc] == 0 and visited[nr][nc][z] == 0:
                    visited[nr][nc][z] = visited[r][c][z] + 1
                    queue.append([nr,nc,z])
    return -1

print(bfs(0,0,0))
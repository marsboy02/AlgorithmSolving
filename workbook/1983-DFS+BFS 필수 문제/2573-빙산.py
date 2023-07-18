import sys
from collections import deque

input = sys.stdin.readline

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]


def bfs(r, c, visited):
    queue = deque()
    queue.append([r, c])
    visited[r][c] = 1
    sea_list = []
    while queue:
        r, c = queue.popleft()
        zero = 0
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if not board[nr][nc]:
                    zero += 1
                elif board[nr][nc] and not visited[nr][nc]:
                    queue.append([nr, nc])
                    visited[nr][nc] = 1
        if zero > 0:
            sea_list.append([r, c, zero])
    for r, c, zero in sea_list:
        board[r][c] = max(0, board[r][c] - zero)
    return


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

year = 0
while True:
    cnt = 0
    visited = [[0] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if board[r][c] > 0 and not visited[r][c]:
                cnt += 1
                bfs(r, c, visited)

    if cnt == 0:
        year = 0
        break
    if cnt > 1:
        break
    year += 1
print(year)

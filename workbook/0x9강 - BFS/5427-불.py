from collections import deque
import sys

input = sys.stdin.readline

dr = [0,0,-1,1]
dc = [-1,1,0,0]

def bfs():
    while queue:
        r,c = queue.popleft()
        if visited[r][c] != "FIRE":
            flag = visited[r][c]
        else:
            flag = "FIRE"

        for i in range(4):
            nr,nc = r+dr[i], c+dc[i]
            if 0 <= nr < h and 0 <= nc < w:
                if visited[nr][nc] == -1 and (
                    board[nr][nc] == '.' or board[nr][nc] == '@'
                    ):
                    if flag == "FIRE":
                        visited[nr][nc] = flag
                    else:
                        visited[nr][nc] = flag + 1
                    queue.append([nr,nc])
            else:
                if flag != "FIRE":
                    return flag + 1
    return "IMPOSSIBLE"

t = int(input())
for _ in range(t):
    w,h = map(int, input().split())
    queue = deque()
    board = []
    visited = [[-1] * w for _ in range(h)]
    for i in range(h):
        board.append(list(input()))
        for j in range(w):
            if board[i][j] == '@':
                visited[i][j] = 0
                start = (i,j)
            elif board[i][j] == '*':
                visited[i][j] = "FIRE"
                queue.append([i,j])
    queue.append(start)
    print(bfs())

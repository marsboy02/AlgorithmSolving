import sys
from collections import deque
input = sys.stdin.readline
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,-1,1]

def bfs(x,y,z):
    queue = deque()
    queue.append([x,y,z])
    cnt[x][y][z] = 1
    while queue:
        x,y,z = queue.popleft()
        for i in range(6):
            nx,ny,nz = x+dx[i],y+dy[i],z+dz[i]
            if 0 <= nx < l and 0 <= ny < r and 0 <= nz < c:
                if board[nx][ny][nz] == 'E':
                    print(f"Escaped in {cnt[x][y][z]} minute(s).")
                    return
                if board[nx][ny][nz] == '.' and cnt[nx][ny][nz] == 0:
                    cnt[nx][ny][nz] = cnt[x][y][z] + 1
                    queue.append([nx,ny,nz])
    print('Trapped!')

while True:
    l,r,c = map(int,input().split())
    if l == r == c == 0:
        break
    board = [[[] * c for _ in range(r)] for _ in range(l)]
    cnt = [[[0] * c for _ in range(r)] for _ in range(l)]
    for i in range(l):
        board[i] = [list(map(str, input().strip())) for _ in range(r)]
        input()
    for i in range(l):
        for j in range(r):
             for k in range(c):
                 if board[i][j][k] == 'S':
                     bfs(i,j,k)
             
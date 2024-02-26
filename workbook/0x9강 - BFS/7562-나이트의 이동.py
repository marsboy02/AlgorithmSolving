from collections import deque

dx = [-1,-2,-2,-1,1,2,2,1]
dy = [2,1,-1,-2,-2,-1,1,2]

def bfs(x1,y1,x2,y2):
    queue = deque()
    queue.append([x1,y1])
    board[x1][y1] = 1

    while queue:
        a,b = queue.popleft()
        if a == x2 and b == y2:
            print(board[x2][y2] - 1)
            return
        for i in range(8):
            nx,ny = a+dx[i], b+dy[i]
            if 0 <= nx < t and 0 <= ny < t and board[nx][ny] == 0:
                queue.append([nx,ny])
                board[nx][ny] = board[a][b] + 1
            
n = int(input())
for i in range(n):
    t = int(input())
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())

    board = [[0] * t for i in range(t)]
    bfs(x1,y1,x2,y2)

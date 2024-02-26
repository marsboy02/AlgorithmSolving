from collections import deque

n = int(input())
board = [list(map(int, input())) for _ in range(n)]

dr = [0,0,-1,1]
dc = [-1,1,0,0]
house = []

def bfs(r,c):
    queue = deque()
    queue.append([r,c])
    board[r][c] = 0
    cnt = 1
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc]:
                queue.append([nr,nc])
                board[nr][nc] = 0
                cnt += 1
    return cnt

for r in range(n):
    for c in range(n):
        if board[r][c]:
            house.append(bfs(r,c))

print(len(house))
print("\n".join(map(str, sorted(house))))
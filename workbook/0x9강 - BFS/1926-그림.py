from collections import deque

n,m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]
_max = 0
_sum = 0
_count = 0

dr = [0,0,-1,1]
dc = [-1,1,0,0]

def bfs(r,c):
    global _sum
    _sum = 0
    queue = deque()
    queue.append([r,c])
    board[r][c] = 0
    while queue:
        _sum += 1
        r,c = queue.popleft()
        for i in range(4):
            nr,nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 1:
                board[nr][nc] = 0
                queue.append([nr,nc])
    return _sum
    

for r in range(n):
    for c in range(m):
        if board[r][c] == 1:
            _count += 1
            _max = max(bfs(r,c), _max)

print(_count)
print(_max)
        

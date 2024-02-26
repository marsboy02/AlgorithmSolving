from collections import deque
import sys

input = sys.stdin.readline
r,c = map(int, input().split())
board = []

q_j = deque()
q_f = deque()

visited_j = [[0] * c for _ in range(r)]
visited_f = [[0] * c for _ in range(r)]

dr = [0,0,-1,1]
dc = [-1,1,0,0]

for i in range(r):
    temp = list(input())
    for j in range(len(temp)):
        if temp[j] == 'J':
            q_j.append((i,j))
            visited_j[i][j] = 1
        elif temp[j] == 'F':
            q_f.append((i,j))
            visited_f[i][j] = 1
            
    board.append(temp)

def bfs():
    while q_f:
        tr,tc = q_f.popleft()
        
        for i in range(4):
            nr,nc = tr+dr[i], tc+dc[i]
            
            if 0 <= nr < r and 0 <= nc < c:
                if not visited_f[nr][nc] and board[nr][nc] != '#':
                    visited_f[nr][nc] = visited_f[tr][tc] + 1
                    q_f.append([nr,nc])

    while q_j:
        tr,tc = q_j.popleft()
        
        for i in range(4):
            nr,nc = tr+dr[i], tc+dc[i]
            
            if 0 <= nr < r and 0 <= nc < c:
                if board[nr][nc] != '#' and not visited_j[nr][nc]:
                    if not visited_f[nr][nc] or visited_f[nr][nc] > visited_j[tr][tc] + 1:
                        visited_j[nr][nc] = visited_j[tr][tc] + 1
                        q_j.append([nr,nc])
            else:
                return visited_j[tr][tc]

    return "IMPOSSIBLE"

print(bfs())

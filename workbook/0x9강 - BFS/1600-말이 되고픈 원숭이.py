from collections import deque
import sys
input = sys.stdin.readline

k = int(input())
w,h = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(h)]
visited = [[0] * w] * h

dr = [0,0,-1,1]
dc = [-1,1,0,0]
kr = [-2,-2,-1,-1,1,1,2,2]
kc = [-1,1,-2,2,-2,2,-1,1]

def bfs(r,c):
    visited = [[[0] * (k+1) for _ in range(w)] for _ in range(h)]
    queue = deque()
    queue.append([r,c,0])
    visited[0][0][0] = 1
    while queue:
        r,c,z = queue.popleft()
        if r == h-1 and c == w-1:
            return visited[r][c][z] - 1

        for i in range(4):
            nr,nc = r+dr[i], c+dc[i]
            if 0 <= nr < h and 0 <= nc < w:
                if not visited[nr][nc][z] and not board[nr][nc]:
                    visited[nr][nc][z] = visited[r][c][z] + 1
                    queue.append([nr,nc,z])
        
        if z < k:
            for i in range(8):
                nr,nc = r+kr[i], c+kc[i]
                if 0 <= nr < h and 0 <= nc < w:
                    if not board[nr][nc] and not visited[nr][nc][z+1]:
                        visited[nr][nc][z+1] = visited[r][c][z] + 1
                        queue.append([nr,nc,z+1])
    return -1

print(bfs(0,0))

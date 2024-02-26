from collections import deque
import sys
input = sys.stdin.readline

n, m, p = map(int, input().split())
s = [0] + list(map(int, input().split()))
gathering = [0] * (p+1)
room = [[0] * m for _ in range(n)]
castle = [deque() for _ in range(p+1)]

dr = [0,0,-1,1]
dc = [-1,1,0,0]

for i in range(n):
    tmp = input().rstrip()
    for j in range(m):
        if tmp[j] == '.':
            room[i][j] = 0
        elif tmp[j] == '#':
            room[i][j] = -1
        else:
            now = int(tmp[j])
            room[i][j] = now
            castle[now].append([i,j])
            gathering[now] += 1

moving = True
while moving:
    moving = False
    for i in range(1, p+1):
        if not castle[i]:
            continue
        queue = castle[i]
        for _ in range(s[i]):
            if not queue:
                break
            for _ in range(len(queue)):
                r, c = queue.popleft()
                now = room[r][c]
                for j in range(4):
                    nr,nc = r+dr[j], c+dc[j]
                    if nr < 0 or nr >= n or nc < 0 or nc >= m:
                        continue
                    if room[nr][nc] == -1:
                            continue
                    if room[nr][nc] > 0:
                            continue
                    room[nr][nc] = now
                    gathering[now] += 1
                    queue.append([nr,nc])
                    moving = True

print(*gathering[1:])
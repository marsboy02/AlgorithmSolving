import sys
from collections import deque
input = sys.stdin.readline

dr = [0,0,-1,1]
dc = [-1,1,0,0]

r,c = map(int, input().split())
maps = [list(input().rstrip()) for _ in range(r)]
swanCheck =[[False] * c for _ in range(r)]
waterCheck = [[False] * c for _ in range(r)]

swanPos = deque()
nextSwanPos = deque()
waterPos = deque()
nextWaterPos = deque()


def waterMelt():
    while waterPos:
        tr, tc = waterPos.popleft()
        maps[tr][tc] = '.'
        for i in range(4):
            nr, nc = tr+dr[i], tc+dc[i]
            if 0 <= nr < r and 0 <= nc < c and not waterCheck[nr][nc]:
                if maps[nr][nc] == '.':
                    waterPos.append([nr,nc])
                elif maps[nr][nc] == 'X':
                    nextWaterPos.append([nr,nc])
                waterCheck[nr][nc] = True


def findSwan():
    while swanPos:
        tr, tc = swanPos.popleft()
        if tr == endR and tc == endC:
            return True
        for i in range(4):
            nr,nc = tr+dr[i], tc+dc[i]
            if 0 <= nr < r and 0 <= nc < c and not swanCheck[nr][nc]:
                if maps[nr][nc] == '.':
                    swanPos.append([nr,nc])
                elif maps[nr][nc] == 'X':
                    nextSwanPos.append([nr,nc])
                swanCheck[nr][nc] = True
    return False


for tr in range(r):
    for tc in range(c):
        if maps[tr][tc] == 'L':
            if not swanPos:
                swanPos.append([tr,tc])
                swanCheck[tr][tc] = True
            else:
                endR, endC = tr, tc
            maps[tr][tc] = '.'

            waterPos.append([tr,tc])
            waterCheck[tr][tc] = True
        
        elif maps[tr][tc] == '.':
            waterPos.append([tr,tc])
            waterCheck[tr][tc] = True

answer = 0
while True:
    waterMelt()
    if findSwan():
        break
    swanPos = nextSwanPos
    waterPos = nextWaterPos
    nextSwanPos = deque()
    nextWaterPos = deque()

    answer += 1

print(answer)
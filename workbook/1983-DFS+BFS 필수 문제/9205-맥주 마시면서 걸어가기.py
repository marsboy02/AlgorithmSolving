import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    queue = deque()
    queue.append(house)
    while queue:
        x, y = queue.popleft()
        if abs(x - festival[0]) + abs(y - festival[1]) <= 1000:
            return 'happy'
        for i in range(n):
            if not visited[i]:
                nx, ny = convenience[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    visited[i] = 1
                    queue.append([nx, ny])
    return 'sad'


t = int(input())
for _ in range(t):
    n = int(input())
    house = list(map(int, input().split()))
    convenience = [list(map(int, input().split())) for _ in range(n)]
    festival = list(map(int, input().split()))
    visited = [0] * (n + 1)
    print(bfs())

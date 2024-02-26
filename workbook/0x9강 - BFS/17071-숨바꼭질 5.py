from collections import deque


MAX = 500000
n,k = map(int,input().split())
visited =[[-1 for _ in range(MAX + 1)] for _ in range(2)]

def bfs(n):
    queue = deque()
    queue.append((n,0))
    visited[0][n] = 0

    while len(queue):
        n, cnt = queue.popleft()
        flag = cnt % 2

        for dx in [n+1, n-1, 2*n]:
            if 0 <= dx <= MAX and visited[1-flag][dx] == -1:
                visited[1-flag][dx] = cnt + 1
                queue.append((dx, cnt+1))
    
bfs(n)

t = 0
flag = 0
res = -1
while k <= 500000:
    if visited[flag][k] != -1:
        if visited[flag][k] <= t:
            res = t
            break
    flag = 1 - flag
    t += 1
    k += t

print(res)
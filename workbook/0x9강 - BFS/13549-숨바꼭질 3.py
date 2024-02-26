from collections import deque

n,k = map(int,input().split())

def bfs(x,k):
    queue = deque()
    queue.append(x)
    check[x] = True
    while queue:
        x = queue.popleft()
        if x == k:
            return dist[k]
        for dx in [2*x, x-1, x+1]:
            if dx <= MAX and check[dx] == False and dx == 2*x:
                dist[dx],check[dx] = dist[x], True
                queue.append(dx)
            elif 0 <= dx <= MAX and check[dx] == False:
                dist[dx], check[dx] = dist[x] + 1, True
                queue.append(dx)


MAX = 100001
dist = [0] * (MAX+1)
check = [False] * (MAX+1)
print(bfs(n,k))

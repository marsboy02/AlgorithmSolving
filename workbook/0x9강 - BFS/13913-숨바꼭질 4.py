from collections import deque

n,k = map(int, input().split())

def move(x):
    data = []
    temp = x
    for _ in range(dist[x]+1):
        data.append(temp)
        temp = check[temp]
    print(' '.join(map(str, data[::-1])))

def bfs(x,k):
    queue = deque([x])
    while queue:
        x = queue.popleft()
        if x == k:
            print(dist[k])
            return move(k)
        for dx in [x-1, x+1, 2*x]:
            if 0 <= dx < MAX and not dist[dx]:
                dist[dx] = dist[x] + 1
                queue.append(dx)
                check[dx] = x


MAX = 100001
dist = [0] * MAX
check = [0] * MAX
bfs(n,k)

n, m = map(int, input().split())
r, c, d = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited[r][c] = True
cnt = 1

while True:
    flag = 0

    for _ in range(4):
        nx, ny = r + dx[(d + 3) % 4], c + dy[(d + 3) % 4]
        d = (d + 3) % 4
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                cnt += 1
                r, c = nx, ny
                flag = 1
                break
    if flag == 0:
        if board[r - dx[d]][c - dy[d]] == 1:
            print(cnt)
            break
        else:
            r, c = r - dx[d], c - dy[d]

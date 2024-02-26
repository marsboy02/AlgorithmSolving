import sys
sys.setrecursionlimit(10**6)

n = int(input())
board = [list(input()) for _ in range(n)]
board_special = []

for r in range(n):
    temp = []
    for c in range(n):
        if board[r][c] == 'R':
            temp.append('G')
        else:
            temp.append(board[r][c])
    board_special.append(temp)

dr = [0,0,-1,1]
dc = [-1,1,0,0]

def dfs(r,c,char, matrix):
    matrix[r][c] = '.'
    for i in range(4):
        nr,nc = r+dr[i], c+dc[i]
        if 0 <= nr < n and 0 <= nc < n and matrix[nr][nc] == char:
            dfs(nr,nc,char, matrix)
            
general = 0
special = 0

for r in range(n):
    for c in range(n):
        if board[r][c] != '.':
            general += 1
            dfs(r,c,board[r][c],board)
        if board_special[r][c] != '.':
            special += 1
            dfs(r,c,board_special[r][c],board_special)

print(general, special)

from collections import deque

m,n,k = map(int, input().split())

board = [[0] * n for _ in range(m)]
for _ in range(k):
    x1,y1,x2,y2 = map(int, input().split())
    
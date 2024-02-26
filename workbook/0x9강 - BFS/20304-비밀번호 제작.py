import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
p = list(map(int, input().split()))
safety = [21 for _ in range(n+1)]
queue = deque()

for i in p:
    safety[i] = 0
    queue.append(i)

answer = 0

while len(queue) != 0:
    cur = queue.popleft()
    for i in range(20):
        x = (1<<i) ^ cur
        if x <= n and safety[cur] + 1 < safety[x]:
            safety[x] = safety[cur] + 1
            answer = max(safety[x], answer)
            queue.append(x)

print(answer)
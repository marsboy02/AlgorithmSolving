import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
li = []

for _ in range(n):
    li.append(int(input()))

li = li[::-1]

for i in range(len(li)-1):
    while li[i] <= li[i+1]:
        li[i+1] -= 1
        cnt += 1

print(cnt)

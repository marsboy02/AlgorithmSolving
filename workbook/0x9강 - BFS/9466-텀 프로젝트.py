import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(x, result):
    visited[x] = True
    cycle.append(x)
    number = li[x]

    if visited[number]:
        if number in cycle:
            result += cycle[cycle.index(number):]
        return
    else:
        dfs(number, result)

for _ in range(int(input())):
    n = int(input())
    li = [0] + list(map(int,input().split()))
    visited = [False] * (n+1)
    result = []

    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i, result)

    print(n - len(result))

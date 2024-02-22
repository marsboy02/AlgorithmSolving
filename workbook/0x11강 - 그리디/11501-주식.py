import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    li = list(map(int, input().split()))

    value, _max = 0,0
    for i in range(n-1, -1 ,-1):
        if (li[i] > _max):
            _max = li[i]
        else:
            value += _max - li[i]
    print(value)

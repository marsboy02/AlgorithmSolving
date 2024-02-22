import sys
input = sys.stdin.readline

n,c = map(int, input().split())
m = int(input())

viliage  = []
for _ in range(m):
    viliage.append(list(map(int,input().split())))
viliage.sort(key= lambda x: x[1])

capa = [c] * n
total = 0
for s, r, box in viliage:
    _min = c
    for i in range(s,r):
        if _min > min(capa[i], box):
            _min = min(capa[i], box)
    for i in range(s, r):
        capa[i] -= _min
    total += _min
print(total)

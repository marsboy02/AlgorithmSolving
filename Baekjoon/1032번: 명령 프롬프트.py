n = int(input())

default = list(input())

for _ in range(n-1):
    line = list(input())
    for i in range(len(line)):
        if default[i] != line[i]:
            default[i] = '?'

print(''.join(default))

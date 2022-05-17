n = int(input())

cnt = 0

while n >= 0:
    if n % 3 == 0:
        cnt -= 3

        exit()
    else:
        n -= 3
        cnt += 1

print(-1)

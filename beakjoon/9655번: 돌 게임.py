n = int(input())

Winner = ['SK', 'CY']
cnt = 0

while n >= 0:
    if n > 3:
        n -= 3
        cnt += 1
    else:
        n -= 1
        cnt += 1

print(Winner[cnt % 2])


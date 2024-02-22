n = int(input())

plus, minus = [], []
result = 0
for _ in range(n):
    n = int(input())
    if n > 1:
        plus.append(n)
    elif n <= 0:
        minus.append(n)
    else:
        result += n

plus.sort(reverse=True)
minus.sort()

for i in range(0, len(plus), 2):
    if i+1 >= len(plus):
        result += plus[i]
    else:
        result += plus[i] * plus[i+1]

for j in range(0, len(minus), 2):
    if j+1 >= len(minus):
        result += minus[j]
    else:
        result += minus[j] * minus[j+1]

print(result)


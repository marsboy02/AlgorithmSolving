n,k = map(int, input().split())
use = list(map(int, input().split()))
code = []
answer = 0

for i in range(k):
    if use[i] in code:
        continue

    if len(code) < n:
        code.append(use[i])
        continue

    priority = []
    for c in code:
        if c in use[i:]:
            priority.append(use[i:].index(c))
        else:
            priority.append(101)
    target = priority.index(max(priority))
    code.remove(code[target])
    code.append(use[i])
    answer += 1

print(answer)

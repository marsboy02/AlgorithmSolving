n = int(input())
li = list(map(int, input().split()))
index = [-1] * (n+1)

for i,v in enumerate(li):
    index[v] = i

longest, cnt = 0, 1
for i in range(1,n):
    if index[i] < index[i + 1]:
        cnt += 1
    else:
        longest = max(longest, cnt)
        cnt = 1

print(n - longest if n != 1 else 0)

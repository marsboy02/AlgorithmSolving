first = []
second = []
for _ in range(3):
    a,b = map(int,input().split())
    first.append(a)
    second.append(b)

first.sort()
second.sort()


for i in range(3):
    if first[i] != first[1]:
        a = first[i]
        
    if second[i] != second[1]:
        b = second[i]

print(a,b)

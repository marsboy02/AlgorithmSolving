n = int(input())
p = []
p = list(map(int,input().split()))
p.sort()
sumn = 0
length = len(p)
for i in range(len(p)):
    sumn += p[i] * length
    length -= 1
    
print(sumn)

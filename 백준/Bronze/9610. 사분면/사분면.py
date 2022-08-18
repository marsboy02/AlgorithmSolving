n = int(input())

li = [0 for _ in range(5)]

for i in range(n):
    a,b = map(int,input().split())

    if a == 0 or b == 0:
        li[4] += 1
    elif a > 0 and b > 0:
        li[0] += 1
    elif a < 0 and b > 0:
        li[1] += 1
    elif a < 0 and b < 0:
        li[2] += 1
    elif a > 0 and b < 0:
        li[3] += 1

for i in range(len(li)-1):
    print('Q'+str(i+1)+': '+str(li[i]))

print('AXIS: '+str(li[4]))

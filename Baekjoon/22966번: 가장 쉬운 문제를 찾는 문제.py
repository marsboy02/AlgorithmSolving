n = int(input())
level = 4 

li = [] #이차원 리스트로 풀이

for i in range(n):
    li.append(list(input().split()))
    
    if int(li[i][1]) <= int(level):
        level = int(li[i][1])
        line = i

print(li[line][0])

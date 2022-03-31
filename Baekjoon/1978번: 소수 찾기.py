n = int(input()) #갯수

li = list(map(int,input().split()))
count = 0

for i in range(len(li)): #리스트 탐색
    check = True
    if li[i] == 1:
        check = False
        
    else:
         for j in range(2, li[i]): #소수 체크
             if li[i] % j == 0:
                 check = False

    if check == True:
        count += 1

print(count)

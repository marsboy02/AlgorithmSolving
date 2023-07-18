li=[]

col = 0     #열
row = 0     #행
maxvalue = 0    #최대값

for i in range(9):
    li.append(list(map(int,input().split())))
    for j in range(9):
        if li[i][j] >= maxvalue:
            maxvalue = li[i][j]
            row = i+1
            col = j+1
    
print("%d\n%d %d" % (maxvalue,row,col))

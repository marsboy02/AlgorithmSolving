import sys
input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    start_m, start_d, end_m, end_d = map(int, input().split())
    li.append([start_m * 100 + start_d, end_m * 100 + end_d])

li.sort()
end_date, count = 301, 0

while li:
    if end_date >= 1201 or li[0][0] > end_date:
        break
    
    temp_end_date = -1

    for _ in range(len(li)):
        if li[0][0] <= end_date:
            if temp_end_date <= li[0][1]:
                temp_end_date = li[0][1]
            li.remove(li[0])
        else:
            break
    
    end_date = temp_end_date
    count += 1

if end_date < 1201:
    print(0)
else:
    print(count)
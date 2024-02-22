n = int(input())
schedule = [list(map(int,input().split())) for _ in range(n)]
schedule.sort(key=lambda x: (x[1],x[0]))

endPoint = 0
answer = 0

for newStart, newEnd in schedule:
    if endPoint <= newStart:
        answer += 1
        endPoint = newEnd
print(answer)

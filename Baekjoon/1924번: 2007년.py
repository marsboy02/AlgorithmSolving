x,y = map(int,input().split())

totaldays = y

months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
          7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
week = ['MON','TUE','WED','THU','FRI','SAT','SUN']
#월마다 있는 일의 날, 1월은 예외처리

for i in range(1,x):
    totaldays += months[i]

print(week[(totaldays-1)%7])

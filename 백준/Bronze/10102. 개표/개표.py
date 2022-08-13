n = int(input())
string = input()

if string.count('A') > string.count('B'):
    print('A')

elif string.count('A') < string.count('B'):
    print('B')

else:
    print('Tie')

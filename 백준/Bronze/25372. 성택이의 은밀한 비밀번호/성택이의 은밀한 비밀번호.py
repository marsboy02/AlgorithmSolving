n = int(input())

for _ in range(n):
    _input = input()
    print('yes' if len(_input) >= 6 and len(_input) <= 9 else 'no')

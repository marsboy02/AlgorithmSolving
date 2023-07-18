import math

n = int(input())

if n == 0:  #예외처리
    print("NO")
    exit()
    
for i in range(30,-1,-1):
    if n >= math.factorial(i):
        n -= math.factorial(i)

if n == 0:
    print("YES")

else:
    print("NO")

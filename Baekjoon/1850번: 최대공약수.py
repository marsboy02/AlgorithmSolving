def gcd(a,b):
    while b:
        a, b = b, a % b
    return a


a,b = map(int, input().split())

print('1' * gcd(a,b))

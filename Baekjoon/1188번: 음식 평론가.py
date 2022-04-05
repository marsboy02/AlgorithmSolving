def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)
#유클리드 호제법
    
n, m = map(int, input().split())
print(m - gcd(n, m))

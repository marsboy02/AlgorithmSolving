n = int(input())
dp = [0] * 1001

dp[1] = 1
dp[3] = 1
dp[4] = 1
if n >= 5:
    for i in range(5, n+1):
        if not dp[i-1]:
            dp[i] = 1
        if not dp[i-3]:
            dp[i] = 1
        if not dp[i-4]:
            dp[i] = 1

print("SK" if dp[n] else "CY")

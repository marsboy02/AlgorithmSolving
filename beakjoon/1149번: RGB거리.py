n = int(input())
dp = []
for i in range(n):
    dp.append(list(map(int,input().split())))
for j in range(1, len(dp)):
    dp[j][0] = min(dp[j-1][1],dp[j-1][2]) + dp[j][0]
    dp[j][1] = min(dp[j-1][0],dp[j-1][2]) + dp[j][1]
    dp[j][2] = min(dp[j-1][0],dp[j-1][1]) + dp[j][2]

print(min(dp[n-1][0],dp[n-1][1],dp[n-1][2]))

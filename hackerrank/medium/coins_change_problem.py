def getWays(n, c):
    c.sort()
    m = len(c)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0]=1
    for i in range(1,m+1):
        for j in range(1,n+1):
            dp[i][j] = dp[i-1][j]
            for k in range(1, j//c[i-1]+1):
                dp[i][j] += dp[i-1][j-k*c[i-1]]
    return dp[-1][-1]

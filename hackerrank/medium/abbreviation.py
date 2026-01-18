def abbreviation(a, b):
    n = len(a)
    m = len(b)
    if m>n:
        return "NO"
    dp = [[False for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0] = True
    for i in range(1,n+1):
        dp[i][0] = dp[i-1][0] and a[i-1].islower()
    
    for i in range(1,n+1):
        a_char = a[i-1]
        for j in range(1,m+1):
            b_char = b[j-1]
            if a_char.isupper():
                dp[i][j] = (a_char==b_char) and dp[i-1][j-1]
            else:
                canCapitalise = (a_char.upper()==b_char) and dp[i-1][j-1]
                canDelete = dp[i-1][j]
                dp[i][j] = canCapitalise or canDelete
    return "YES" if dp[n][m] else "NO"


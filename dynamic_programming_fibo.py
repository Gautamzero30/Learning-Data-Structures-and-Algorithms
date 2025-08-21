# Top-Down (Memoization)
def fib_memo(n, dp={}):
    if n <= 1:
        return n
    if n in dp:
        return dp[n]
    dp[n] = fib_memo(n-1, dp) + fib_memo(n-2, dp)
    return dp[n]

# Bottom-Up (Tabulation)
def fib_tab(n):
    dp = [0, 1] + [0]*(n-1)
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(fib_memo(10))  # 55
print(fib_tab(10))   # 55

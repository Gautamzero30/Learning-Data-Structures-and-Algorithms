def knapsack(W, wt, val, n):
    # dp[i][w] = max value with first i items and capacity w
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):  # items
        for w in range(1, W + 1):  # capacity
            if wt[i - 1] <= w:  # can take item i-1
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]],
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


# -------- Driver code --------
n = int(input("Enter number of items: "))
wt = list(map(int, input("Enter weights: ").split()))
val = list(map(int, input("Enter values: ").split()))
W = int(input("Enter bag capacity: "))

print("Maximum Profit =", knapsack(W, wt, val, n))

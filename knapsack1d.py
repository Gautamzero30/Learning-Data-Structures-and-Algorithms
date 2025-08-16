def knapsack(W, wt, val, n):
    dp = [0] * (W + 1)

    # Process each item
    for i in range(n):
        # Traverse backwards so we don't reuse the same item multiple times
        for w in range(W, wt[i] - 1, -1):
            dp[w] = max(dp[w], val[i] + dp[w - wt[i]])

    return dp[W]


# -------- Driver code --------
n = int(input("Enter number of items: "))
wt = list(map(int, input("Enter weights: ").split()))
val = list(map(int, input("Enter values: ").split()))
W = int(input("Enter bag capacity: "))

print("Maximum Profit =", knapsack(W, wt, val, n))

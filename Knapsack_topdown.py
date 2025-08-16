def knapsack_recursive(W, wt, val, n, memo={}):
    if (n, W) in memo:
        return memo[(n, W)]
    
    if n == 0 or W == 0:  # base case
        return 0

    if wt[n-1] <= W:
        include = val[n-1] + knapsack_recursive(W - wt[n-1], wt, val, n-1, memo)
        exclude = knapsack_recursive(W, wt, val, n-1, memo)
        memo[(n, W)] = max(include, exclude)
    else:
        memo[(n, W)] = knapsack_recursive(W, wt, val, n-1, memo)

    return memo[(n, W)]


# -------- Driver code --------
n = int(input("Enter number of items: "))
wt = list(map(int, input("Enter weights: ").split()))
val = list(map(int, input("Enter values: ").split()))
W = int(input("Enter bag capacity: "))

print("Maximum Profit =", knapsack_recursive(W, wt, val, n))

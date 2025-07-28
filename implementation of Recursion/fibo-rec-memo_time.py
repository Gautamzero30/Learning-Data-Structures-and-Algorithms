import time

def fibonacci_memo(n, memo={}):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


n = int(input("Enter the value of n: "))


start = time.time()
result = fibonacci_memo(n)
end = time.time()

print(f"The {n}th Fibonacci number is: {result}")
print(f"Function execution time (manual memo): {end - start:.6f} seconds")

import time

def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

try:
    n = int(input("Enter the value of n: "))
    start = time.time()
    result = fibonacci(n)
    end = time.time()

    print(f"The {n}th Fibonacci number is: {result}")
    print(f"Function execution time: {end - start:.6f} seconds")
except ValueError:
    print("Please enter a valid integer.")

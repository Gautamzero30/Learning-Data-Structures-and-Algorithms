import time

def fibonacci_recursive(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

try:
    n = int(input("Enter the value of n: "))
    start = time.time()
    result = fibonacci_recursive(n)
    end = time.time()

    print(f"The {n}th Fibonacci number is: {result}")
    print(f"Function execution time: {end - start:.6f} seconds")
except ValueError:
    print("Please enter a valid integer.")


#    Version	Time Complexity	Space Complexity	Max Safe n
# Recursive (basic)	O(2^n)	O(n) call stack	~35–40
# Recursive + Memo	O(n)	O(n)	100,000+
# Iterative	O(n)	O(1)	100,000+

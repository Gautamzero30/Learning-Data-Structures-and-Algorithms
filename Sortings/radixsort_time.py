import random
import time

def radix(a):    
    n = len(a)
    max_num = max(a)
    val = 1
    while max_num // val > 0:
        radix_sort(a, val, n)
        val *= 10

def radix_sort(a, val, n):
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = (a[i] // val) % 10
        count[index] += 1 
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = (a[i] // val) % 10
        output[count[index] - 1] = a[i]
        count[index] -= 1
        i -= 1
    for i in range(n):
        a[i] = output[i]

n = int(input("Enter the number of elements to be sorted: "))
min_val = int(input("Enter the minimum possible value: "))
max_val = int(input("Enter the maximum possible value: "))

a = [random.randint(min_val, max_val) for _ in range(n)]

print("\nOriginal array:")
print(a)

start = time.time()
radix(a)
end = time.time()

print("\nSorted array:")
print(a)
print(f"\nTime taken to sort {n} elements: {end - start:.6f} seconds")

import time
import random

def shellsort(a):
    n = len(a)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap
            a[j] = temp
        gap //= 2
    return a

n = int(input("Enter the number of random elements to sort: "))
min_val = int(input("Enter the minimum possible value: "))
max_val = int(input("Enter the maximum possible value: "))

a = [random.randint(min_val, max_val) for _ in range(n)]

print("\nOriginal array:")
print(a)

start_time = time.time()

shellsort(a)

end_time = time.time()

print("\nSorted array:")
print(a)
print(f"\nTime taken to sort {n} elements: {end_time - start_time:.6f} seconds")

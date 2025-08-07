def quickshort(a, l, r):
    if l < r:
        p = partition(a, l, r)
        quickshort(a, l, p - 1)
        quickshort(a, p + 1, r)

def partition(a, l, r):
    x = l + 1
    y = r
    pivot = a[l]
    while x <= y:
        while x <= r and a[x] <= pivot:
            x += 1
        while a[y] > pivot:
            y -= 1
        if x < y:
            a[x], a[y] = a[y], a[x]
            print("Swapped:", a)
        else:
            break
    a[l], a[y] = a[y], a[l]
    return y

# Input
a = []
n = int(input("Enter the number of elements you want to sort: "))
for i in range(n):
    p = int(input(f"Enter the {i + 1} element: "))
    a.append(p)

quickshort(a, 0, n - 1)
print("The sorted list is", a)

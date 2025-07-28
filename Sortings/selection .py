data = []
n = int(input("enter the numbers of elements to be sorted: "))
for i in range(n):
    x = int(input(f"enter the {i +1} number: "))
    data.append(x)

for i in range(n):
    pos = i
    for j in range(i+1, n):
        if data[j] < data[pos]:
            pos = j
    if i != pos:
        data[i], data[pos] = data[pos], data[i]
print("sorted list is:", data)

